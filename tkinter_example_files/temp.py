import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(True, True)

def pressme(*args):
    print('hi')
b = tkinter.Button(window, text='press me',
                   command=pressme)
b.pack()

window.bind('1', pressme)
window.bind('2', pressme)
window.bind('3', pressme)

window.mainloop()