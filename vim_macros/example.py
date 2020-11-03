"""
We're going to run a trivial example involving modifying a block code. The code itself
will not run.
"""


for house in houses:
    house.colour = config.get("colour", "black")
    house.num_windows = config.get("num_windows", 20)
    house.num_doors = config.get("num_doors", 3)
    house.architecture = config.get("architecture", "adobe revival")


"""
Let's say we want to change this to no longer specify defaults. On line 20, run:
    qr0f=f.ct"[<Esc>f,c$]<Esc>j@rq. Then, go down a line and run @r
"""

for house in houses:
    house.colour = config.get("colour", "black")
    house.num_windows = config.get("num_windows", 20)
    house.num_doors = config.get("num_doors", 3)
    house.architecture = config.get("architecture", "adobe revival")

"""
You should end up with:
"""

for house in houses:
    house.colour = config["colour"]
    house.num_windows = config["num_windows"]
    house.num_doors = config["num_doors"]
    house.architecture = config["architecture"]

"""
Breaking it down. 

qr: Record a macro on key "r"
0: beginning of the line
f=: Jump to the next "="
f.: Jump to the next "."
ct"[<Esc>: Change to the next '"' with a "[" and return to normal mode
f,: Jump to the next ","
c$]<Esc>: Change to the end of the line with a "]" and return to normal mode
j: Down one line
@r: Repeat the macro (recursive)
q: Stop recording the macro.

@r: Run the macro on key "r"
"""
