from tkinter import Tk, Label, Canvas
from graph import create_centers, create_nodes, update_nodes


class GUI:
    def __init__(self, master):
        self.master = master
        self.CENTER_NB = 5
        self.CENTER_SIZE = 20
        self.NODE_NB = 1000
        self.NODE_SIZE = 10
        self.centers = []
        self.centers_states = [{'color': 'red'} for _ in range(self.CENTER_NB)]
        self.nodes = []
        self.pos = (0, 0, 900, 900)  # (minx, miny, maxx, maxy)
        self.selected_center = None

        master.title("Data viz GUI")

        self.label = Label(master, text="Data viz with Tkinter")
        self.label.pack()
        self.canvas = Canvas(master, width=900, height=900, bg="ivory")
        self.canvas.pack()

        self.create_centers(self.CENTER_NB)
        self.create_nodes(self.NODE_NB)

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
                                    width=3, fill=color)

        for i in range(len(self.centers)):
            c = self.centers[i]
            self.canvas.create_oval(c[0], c[1],
                                    c[0]+self.CENTER_SIZE, c[1]+self.CENTER_SIZE,
                                    width=3, fill=self.centers_states[i]['color'])

    def motion(self, event):

        x, y = event.x, event.y

        if self.selected_center is None:
            for i in range(len(self.centers)):
                c = self.centers[i]
                if c[0] < x < c[0]+self.CENTER_SIZE and c[1] < y < c[1] + self.CENTER_SIZE:
                    self.centers_states[i]['color'] = 'blue'
                    self.selected_center = i
                    self.canvas.delete("all")
                    self.draw()

                    break
        else:
            self.centers[self.selected_center][0] = x
            self.centers[self.selected_center][1] = y
            self.centers_states[self.selected_center]['color'] = 'red'
            self.selected_center = None

            self.nodes = update_nodes(self.centers, self.nodes)

            self.canvas.delete("all")
            self.draw()


root = Tk()
gui = GUI(root)
root.bind('<Button-1>', gui.motion)
root.geometry("1000x1000")
gui.draw()
root.mainloop()
