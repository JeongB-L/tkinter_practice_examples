import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(True, True)

temp = [r"{ho}"]
l = tkinter.Label(window, text=temp)
l.pack()



window.mainloop()
