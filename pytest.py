import tkinter as tk

class Ball:
    def __init__(self, canvas, x, y, dx, dy, radius, color):
        self.canvas = canvas
        self.id = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
        self.dx = dx
        self.dy = dy

    def move(self):
        coords = self.canvas.coords(self.id)
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        if coords[0] + self.dx < 0 or coords[2] + self.dx > width:
            self.dx *= -1
        if coords[1] + self.dy < 0 or coords[3] + self.dy > height:
            self.dy *= -1
        self.canvas.move(self.id, self.dx, self.dy)

class Pinball:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()
        self.ball = Ball(self.canvas, 250, 250, 5, 5, 20, "red")
        self.canvas.bind_all("<Button-1>", self.start_game)
        self.score = 0
        self.score_text = self.canvas.create_text(50, 10, text=f"Score: {self.score}")

    def start_game(self, event):
        self.canvas.unbind_all("<Button-1>")
        while True:
            self.ball.move()
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.master.update()
            if self.ball.hit_paddle():
                self.score += 1

root = tk.Tk()
game = Pinball(root)
root.mainloop()
