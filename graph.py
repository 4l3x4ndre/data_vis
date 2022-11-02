import random
from PIL import Image, ImageDraw, ImageFont
from node import Node

SIZE = 20
SIZE_CENTER = 40


def create_centers(center_number, pos):
    centers = []
    for i in range(center_number):
        centers.append([random.randint(pos[0], pos[2]), (i+1) * pos[3] / center_number])
    return centers


def create_nodes(centers, n):
    nodes = []
    for i in range (n):
        x = 0
        y = 0
        values = []

        for v in range (len(centers)):
            value = random.randint(0, 100) / 100
            values.append(value)

            x += value*centers[v][0]
            y += value*centers[v][1]

        x = x / sum(values)
        y = y / sum(values)

        nodes.append(Node(values, (x, y)))

    return nodes


def create_image(centers, nodes):
    # create an image
    out = Image.new("RGB", (2000, 2000), (255, 255, 255))

    # get a drawing context
    d = ImageDraw.Draw(out)

    # draw nodes
    for i in range(len(nodes)):
        n = nodes[i]

        d.ellipse((n.position[0], n.position[1], n.position[0]+SIZE, n.position[1]+SIZE),
               fill=(int(n.position[0] * 255/1500), int(n.position[1] * 255/1500), 255))

        d.text((n.position[0], n.position[1]), str(i),
               fill=(0, 0, 0))

    # draw centers
    for i in range(len(centers)):
        c = centers[i]
        d.ellipse((c[0], c[1], c[0]+SIZE_CENTER, c[1]+SIZE_CENTER), fill=(0, 0, 0), outline=(0, 0, 0))

    out.show()
