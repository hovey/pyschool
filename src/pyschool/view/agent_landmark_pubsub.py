import matplotlib.pyplot as plt
from numpy.random import randint

from pyschool.pattern.publish_subscribe import Publisher
from pyschool.pattern.publish_subscribe import Subscriber

instructions = """
  'r' refresh initial positions
  'q' quit demonstration

  'j' move agent down
  'k' move agent up

  'h' move agent left
  'l' move agent right
  """


# configuration for the world
x_min = 0.0  # lower horizontal bound of view
x_max = 10.0  # upper horizontal bound of view
y_min = 0.0  # lower vertical bound of view
y_max = 10.0  # upper vertical bound of view

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
    # def __init__(self, disp, x, y, type="l"):
    def __init__(self, disp, x, y):
        self.disp = disp
        self.x = x
        self.y = y


class World(Subscriber):
    def __init__(self, ax):
        self.ax = ax
        ax.set_ylim([y_min, y_max])
        ax.set_xlim([x_min, x_max])
        ax.set_aspect(1.0)

        # agent
        box_a_x = randint(low=x_min, high=x_max)
        box_a_y = randint(low=y_min, high=y_max)

        # landmark
        box_b_x = randint(low=x_min, high=x_max)
        box_b_y = randint(low=y_min, high=y_max)

        # boxes
        (boxA,) = self.ax.barh(
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
        (boxB,) = self.ax.barh(
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
        self.instructions = self.ax.annotate(
            instructions,
            (0.5, 0.5),  # middle of view
            verticalalignment="center",
            horizontalalignment="center",
            multialignment="left",
            textcoords="axes fraction",
            animated=False,
        )
        self.canvas.mpl_connect("key_press_event", self.on_key_press)

    def publication_callback(self, *, message: str):  # Subscriber implementation
        super().publication_callback(message=message)
        self.instructions = self.ax.annotate(
            message,
            (0.5, 0.5),  # middle of view
            verticalalignment="center",
            horizontalalignment="center",
            multialignment="left",
            textcoords="axes fraction",
            animated=False,
        )

    def draw(self, event):
        # draw_artist = self.ax.draw_artist
        if self.background is None:
            self.background = self.canvas.copy_from_bbox(self.ax.bbox)

        # restart the clean slate background
        self.canvas.restore_region(self.background)

        # boxes
        for box in self.boxes:
            box.disp.set_y(box.y)
            box.disp.set_x(box.x)
            self.ax.draw_artist(box.disp)

        self.canvas.blit(self.ax.bbox)
        self.canvas.flush_events()

        return True

    def on_key_press(self, event):

        if event.key == "j":  # move down
            self.boxes[0].y -= delta_y
            # enforce lower bounds
            if self.boxes[0].y < y_min:
                self.boxes[0].y = y_min

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
            self.boxes[0].x = randint(low=x_min, high=x_max)
            self.boxes[0].y = randint(low=y_min, high=y_max)

            self.boxes[1].x = randint(low=x_min, high=x_max)
            self.boxes[1].y = randint(low=y_min, high=y_max)

        if event.key == "q":
            # close the figure, end the interactive demonstration
            plt.close()


# main

fig, ax = plt.subplots()
canvas = ax.figure.canvas
animation = World(ax)

# pubsub hook up
verbosity = True
pub = Publisher()

# The World, a subscriber, subscribes to the publisher.
pub.subscribe(animation)

# The publisher publishes to subscribers.
pub.publish(pub.events.publication)

# disable default key bindings by override
if fig.canvas.manager.key_press_handler_id is not None:
    canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)


# # reset the blitting background on redraw
# def on_redraw(event):
#     animation.background = None


# bootstrap after the first draw
def start_anim(event):
    canvas.mpl_disconnect(start_anim.cid)

    def local_draw():
        if animation.ax.get_renderer_cache():
            animation.draw(None)

    start_anim.timer.add_callback(local_draw)
    start_anim.timer.start()
    # canvas.mpl_connect("draw_event", on_redraw)


# draw event from plot gets triggered, map it to call start_anim
start_anim.cid = canvas.mpl_connect("draw_event", start_anim)
start_anim.timer = animation.canvas.new_timer(interval=1)

# plt.show(block=False)
plt.show()
