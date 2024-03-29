import matplotlib.pyplot as plt
from numpy.random import randint
from datetime import datetime

from pyschool.pattern.publish_subscribe import Publisher
from pyschool.pattern.publish_subscribe import Subscriber


# configuration for the world
x_min = 0.0  # lower horizontal bound of view
x_max = 10.0  # upper horizontal bound of view
y_min = 0.0  # lower vertical bound of view
y_max = 10.0  # upper vertical bound of view

x_mid = (x_max - x_min) / 2.0 + x_min
y_mid = (y_max - y_min) / 2.0 + y_min

steps_per_span = 10  # number of discrete points per span in either x or y direction
delta_x = (x_max - x_min) / steps_per_span  # magnitude of x-direction step size
delta_y = (y_max - y_min) / steps_per_span  # magnitude of y-direction step size

# configuration for items in the world
al = 0.5  # alpha

box_width = delta_x  # width, as a fraction of the world x-dimension
box_height = delta_y  # height, as a fraction of the world y-dimension

color_agent = "green"
color_landmark = "black"

lw = 2  # linewidth


class Box:
    def __init__(self, rectangle, x, y):
        # rectangle is a matplotlib.pathes.Rectangle object
        self.rectangle = rectangle
        self.x = x
        self.y = y


class World(Subscriber):
    def __init__(self, ax):
        self.ax = ax
        ax.set_ylim([y_min, y_max])
        ax.set_xlim([x_min, x_max])
        ax.set_aspect(1.0)

        # agent initial position
        box_a_x = randint(low=x_min, high=x_max)
        box_a_y = randint(low=y_min, high=y_max)

        # landmark initial position
        box_b_x = randint(low=x_min, high=x_max)
        box_b_y = randint(low=y_min, high=y_max)

        # boxes
        boxA, *_ = self.ax.barh(
            box_a_y,
            box_width,
            height=box_height,
            color=color_agent,
            alpha=al,
            edgecolor=color_agent,
            linewidth=lw,
            label="Agent",
            animated=True,
        )
        boxB, *_ = self.ax.barh(
            box_b_y,
            box_width,
            height=box_height,
            left=box_b_x,
            color=color_landmark,
            alpha=al,
            edgecolor=color_landmark,
            linewidth=lw,
            label="Landmark",
            animated=True,
        )
        self.canvas = self.ax.figure.canvas
        self.background = None
        self.boxes = [Box(boxA, box_a_x, box_a_y), Box(boxB, box_b_x, box_b_y)]

        # number of times the subscriber callback has been triggered by publisher
        self.num_publication_callbacks = 0

        self.instructions_string = str(
            "\nInstructions:\n\n'r' refresh initial positions\n'q' quit demonstration\n\nAgent always falls down.\n\n'k' move agent up\n'h' move agent left\n'l' move agent right"
        )

        self.instructions = self.ax.annotate(
            text=self.instructions_string,
            xy=(x_mid, y_mid),  # middle of view
            verticalalignment="center",
            horizontalalignment="center",
            multialignment="left",
            animated=False,
        )
        self.canvas.mpl_connect("key_press_event", self.on_key_press)

    def update_title(self):
        now = datetime.now()
        # now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        now_string = "Title updated at " + now.strftime("%H:%M:%S")
        callback_string = f", {self.num_publication_callbacks} callbacks"
        self.ax.set_title(now_string + callback_string)
        # axes.figure.canvas.draw()  # unnecessary because there is a draw timer that triggers

    def publication_callback(self, *, message: str):  # Subscriber implementation
        super().publication_callback(message=message)
        self.num_publication_callbacks += 1

        # every time there is a publication, the agent moves down
        self.boxes[0].y -= delta_y
        # enforce lower bounds
        if self.boxes[0].y < y_min:
            self.boxes[0].y = y_min

    def draw(self, event):
        if self.background is None:
            self.background = self.canvas.copy_from_bbox(self.ax.bbox)

        # restart the clean slate background
        self.canvas.restore_region(self.background)

        self.ax.draw_artist(self.instructions)
        self.canvas.blit(self.ax.bbox)
        self.canvas.flush_events()

        # boxes
        for box in self.boxes:
            box.rectangle.set_y(box.y)
            box.rectangle.set_x(box.x)
            self.ax.draw_artist(box.rectangle)

        self.canvas.blit(self.ax.bbox)
        self.canvas.flush_events()

        return True

    def on_key_press(self, event):

        if event.key == "k":  # move up
            self.boxes[0].y += delta_y
            # enforce upper bounds
            if self.boxes[0].y > y_max - box_height:
                self.boxes[0].y = y_max - box_height

        if event.key == "h":  # move left
            self.boxes[0].x -= delta_x
            # enforce left bounds
            if self.boxes[0].x < x_min:
                self.boxes[0].x = x_min

        if event.key == "l":  # move right
            self.boxes[0].x += delta_x
            # enforce left bounds
            if self.boxes[0].x + box_width > x_max:
                self.boxes[0].x = x_max - box_width

        if event.key == "r":  # refresh initial positions
            # not need, e.g., high=x_max - box_width because the right hand side
            # interval is exclusive, not inclusive
            self.boxes[0].x = randint(low=x_min, high=x_max)
            self.boxes[0].y = randint(low=y_min, high=y_max)

            self.boxes[1].x = randint(low=x_min, high=x_max)
            self.boxes[1].y = randint(low=y_min, high=y_max)

        if event.key == "q":  # quit
            # close the figure, end the interactive demonstration
            plt.close()


# main

fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = World(ax)


# disable default key bindings by override
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# # reset the blitting background on redraw
# def on_redraw(event):
#     animation.background = None


# bootstrap after the first draw
# def start_anim(event):
#     canvas.mpl_disconnect(start_anim.cid)
#
#     def local_draw():
#         if animation.ax.get_renderer_cache():
#             animation.draw(None)
#
#     start_anim.timer.add_callback(local_draw)
#     start_anim.timer.start()
#     # canvas.mpl_connect("draw_event", on_redraw)
#
#
# # draw event from plot gets triggered, map it to call start_anim
# start_anim.cid = canvas.mpl_connect("draw_event", start_anim)
# start_anim.timer = animation.canvas.new_timer(interval=1)


draw_update_interval = 10  # milliseconds
draw_timer = fig.canvas.new_timer(interval=draw_update_interval)
draw_timer.add_callback(animation.draw, None)  # draw updates the world every interval
draw_timer.start()

# Publish-Subscribe
verbosity = True
pub = Publisher()
# The World, a subscriber, subscribes to the publisher.
pub.subscribe(animation)

# The publisher publishes to subscribers.
# hold off on publication until now, will want to queue a publication every x seconds
# pub.publish(pub.events.publication)

# Simulate calculations as the bottleneck, so they take longer than view updates
# calc_timer_interval = 500  # milliseconds, for a fast simulation
calc_timer_interval = 4000  # milliseconds, for a slow simulation
calc_timer = fig.canvas.new_timer(interval=calc_timer_interval)
calc_timer.add_callback(
    pub.publish, pub.events.publication
)  # draw updates the world every interval
calc_timer.start()

# Put view timer after the calculation timer so that the number of pubsub updates is
# always current.
view_update_interval = 1000  # milliseconds, keep as 1 second, like a stopwatch tick
view_timer = fig.canvas.new_timer(interval=view_update_interval)
# view_timer.add_callback(update_title, ax)  # view updates the title every interval
view_timer.add_callback(animation.update_title)  # view updates the title every interval
# view_timer.add_callback(animation.draw, None)  # view updates the world every interval
view_timer.start()

# # bootstrap after the first draw
# def start_anim(event):
#     canvas.mpl_disconnect(start_anim.cid)
#
#     def local_draw():
#         if animation.ax.get_renderer_cache():
#             animation.draw(None)
#
#     start_anim.timer.add_callback(local_draw)
#     start_anim.timer.start()
#     # canvas.mpl_connect("draw_event", on_redraw)
#
#
# # draw event from plot gets triggered, map it to call start_anim
# start_anim.cid = canvas.mpl_connect("draw_event", start_anim)
# draw_update_interval = 10  # milliseconds, should be something very fast
# start_anim.timer = fig.canvas.new_timer(interval=draw_update_interval)

# plt.show(block=False)
plt.show()
