import basic
import tkinter

window = basic.window_setup().window

canvas = tkinter.Canvas(window, relief='solid', bd=2)

line = canvas.create_line(10, 10, 20, 20, 20, 130, 30, 140, fill='red')
# 각 create된 것들은 variable에 저장되나 동시에 캔버스에 추가됨
polygon = canvas.create_polygon(50, 50, 170, 170, 100, 170, outline='yellow')

oval = canvas.create_oval(100, 200, 150, 250, width=4) # width는 테두리의 두꺠

arc = canvas.create_arc(100, 100, 300, 24, start=0, extent=150, fill='green')
canvas.pack()
window.mainloop()