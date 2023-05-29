import basic
import tkinter as tk

window = basic.window_setup().window
window.title('photoimage practice window')



image = tk.PhotoImage(file='Tkinker_practice_files\src\박지옷.PNG')

label = tk.Label(window, image=image)
label.pack()

crr_width = 1

def drawing(event):
    if crr_width > 0:
        x1 = event.x - 1
        y1 = event.y - 1
        x2 = event.x + 1
        y2 = event.y + 1
        canvas.create_oval(x1, y1, x2, y2, fill='blue', width=crr_width)

def scroll(event):
    global crr_width
    if event.delta == 120:
        crr_width += 1
    if event.delta == -120:
        crr_width -= 1
    label1.config(text=str(crr_width))
    
def draw_circle(event):
    global crr_width
    x1 = event.x
    y1 = event.y
    x2 = event.x + crr_width
    y2 = event.y + crr_width
    canvas.create_arc(x1, y1, x2, y2)
    
canvas = tk.Canvas(window, relief='solid', bd=2)
canvas.pack(expand=True, fill='both')
canvas.bind('<B1-Motion>', drawing) # 각 눌리는 키보드 버튼에 따라서 function을 binding 할
                                    # 수 있음
canvas.bind('<MouseWheel>', scroll)
canvas.bind('<Button-1>', draw_circle)

label1 = tk.Label(window, text=str(crr_width))
label1.pack()

window.mainloop()