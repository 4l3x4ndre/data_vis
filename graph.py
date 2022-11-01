import random
from PIL import Image, ImageDraw, ImageFont
from node import Node

CENTER_NUMBER = 5
N = 1000
SIZE = 20
SIZE_CENTER = 40

centers = []
nodes = []

for i in range(CENTER_NUMBER):
    centers.append([random.randint(0, 1500), (i+1)*1500/CENTER_NUMBER])

# create nodes
for i in range (N):
    x = 0
    y = 0
    values = []

    for v in range (CENTER_NUMBER):
        value = random.randint(0, 100) / 100
        values.append(value)

        x += value*centers[v][0]
        y += value*centers[v][1]

    x = x / sum(values)
    y = y / sum(values)

    nodes.append(Node(values, (x, y)))

# create an image
out = Image.new("RGB", (2000, 2000), (255, 255, 255))

# get a drawing context
d = ImageDraw.Draw(out)

# draw nodes
for i in range(len(nodes)):
    n = nodes[i]

    d.ellipse((n.position[0], n.position[1], n.position[0]+SIZE, n.position[1]+SIZE),
           fill=(int(n.position[0] * 255/1500), int(n.position[1] * 255/1500), 128))

    d.text((n.position[0], n.position[1]), str(i),
           fill=(0, 0, 0))


# draw centers
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 255), (0, 0, 255)]
for i in range(len(centers)):
    c = centers[i]
    d.ellipse((c[0], c[1], c[0]+SIZE_CENTER, c[1]+SIZE_CENTER), fill=(0, 0, 0), outline=(0, 0, 0))

out.show()
