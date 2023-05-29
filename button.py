import tkinter

window = tkinter.Tk()

counter = 0

def countUp():
    global counter
    counter +=1
    button_description.config(text=str(counter))

window.title("practicing button")
window.resizable(True, True)
window.geometry("400x400+100+100")

button_description = tkinter.Label(window, text="0")
button_description.pack()

text_on_button = "hello world"

button = tkinter.Button(window,text=text_on_button, overrelief="solid", width=15, repeatdelay=1000,
                        repeatinterval=100, activebackground="red", takefocus=True)

button['command'] = countUp

button.pack()
# tmep

window.mainloop()