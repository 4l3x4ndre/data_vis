from tkinter import  Tk, Label, Canvas
from graph import create_centers, create_nodes


class GUI:
    def __init__(self, master):
        self.master = master
        self.centers = []
        self.nodes = []
        self.CENTER_SIZE = 20
        self.NODE_SIZE = 10
        self.pos = (0, 0, 800, 800) # (minx, miny, maxx, maxy)

        master.title("Data viz GUI")

        self.label = Label(master, text="Data viz with Tkinter")
        self.label.pack()
        self.canvas = Canvas(master, width=900, height=900, bg="ivory")
        self.canvas.pack()

        self.create_centers(5)
        self.create_nodes(1000)

    def create_centers(self, n):
        self.centers = create_centers(n, self.pos)

    def create_nodes(self, n):
        self.nodes = create_nodes(self.centers, n)

    def draw(self):
        for i in range(len(self.nodes)):
            n = self.nodes[i]

            color = '#%02x%02x%02x' % (
                int(n.position[0] * 255/self.pos[3]),
                int(n.position[1] * 255/self.pos[3]),
                150
            )

            # (x1, x2, y1, y2)
            self.canvas.create_oval(n.position[0], n.position[1],
                                    n.position[0]+self.NODE_SIZE, n.position[1]+self.NODE_SIZE,
                                    width = 3, fill=color)

        for i in range(len(self.centers)):
            c = self.centers[i]
            self.canvas.create_oval(c[0], c[1],
                                    c[0]+self.CENTER_SIZE, c[1]+self.CENTER_SIZE,
                                    width = 3, fill="red")


root = Tk()
gui = GUI(root)
root.geometry("1000x1000")
gui.draw()
root.mainloop()
