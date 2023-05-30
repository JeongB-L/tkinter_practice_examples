import basic
import tkinter
import tkinter.ttk

window = basic.window_setup().window
window.title('this is a sizegrip practice')

#위젯 크기를 조절하는 작은 버튼 생성
def drag(event):
# winfo means widget information
    x=sizegrip.winfo_x()+event.x
    y=sizegrip.winfo_y()+event.y
    sz_width=sizegrip.winfo_reqwidth()
    sz_height=sizegrip.winfo_reqheight()

    text["width"]=x-sz_width
    text["height"]=y-sz_height

    if x >= sz_width and y >= sz_height and x < window.winfo_width() and y < window.winfo_height():
        text.place(x=0, y=0, width=x, height=y)
        sizegrip.place(x=x-sz_width, y=y-sz_height)

text = tkinter.Text(window)
text.place(x=0, y=0)
    
sizegrip = tkinter.ttk.Sizegrip(window)
sizegrip.place(x=text.winfo_reqwidth() - sizegrip.winfo_reqheight(), 
               y=text.winfo_reqheight() - sizegrip.winfo_reqheight())
sizegrip.bind("<B1-Motion>", drag)


window.mainloop()