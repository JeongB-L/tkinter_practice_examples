import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(True, True)

def pressme(event):
    print('hi')
    l.config(text=event.char)
    
l = tkinter.Label(window, text='here')
l.pack()

window.bind('<Key>', pressme)

window.mainloop()