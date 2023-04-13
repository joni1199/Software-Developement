import tkinter as tk

def create_rounded_rect(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True, tags='button')

def button_clicked(event):
    print('Button clicked!')

root = tk.Tk()
canvas = tk.Canvas(root, width=100, height=50, highlightthickness=0)
canvas.pack()

button = create_rounded_rect(canvas, 10, 10, 90, 40, 10, fill='blue')
text = canvas.create_text(50, 25, text='0', fill='white', tags='button')

canvas.tag_bind('button', '<Button-1>', button_clicked)

root.mainloop()