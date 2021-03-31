# configure_font.py

import matplotlib.pyplot as plt
from matplotlib import rcParams

# >>> rcParams["font.family"]
# ['sans-serif']
# >>> rcParams["font.serif"]
# ['DejaVu Serif', 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook', 'Century Schoolbook L', 'Utopia', 'ITC Bookman', 'Bookman', 'Nimbus Roman No9 L', 'Times New Roman', 'Times', 'Palatino', 'Charter', 'serif']
# >>> rcParams["font.sans-serif"]
# ['DejaVu Sans', 'Bitstream Vera Sans', 'Computer Modern Sans Serif', 'Lucida Grande', 'Verdana', 'Geneva', 'Lucid', 'Arial', 'Helvetica', 'Avant Garde', 'sans-serif']
#

rcParams["font.family"] = "serif"
rcParams["font.sans-serif"] = ["Bookman"]

fig, ax = plt.subplots()
ax.plot([1, 2, 5], label="test")

ax.legend()
plt.show()
