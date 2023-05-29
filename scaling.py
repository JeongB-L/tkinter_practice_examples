import basic
import tkinter

window = basic.window_setup().window
window.title('scrollbar practice for scale')

var = tkinter.IntVar()

def selecto(self):
    value='value: ' + str(scale.get())
    label.config(text=value)
    
counter = 0

def temp(self): # self 인자, 그러니까 스스로를 참조 해야 하는 command parameter가 scale에는 존재하나
    # 버튼에는 self를 필요로 하지 않음
    global counter
    counter += 1
    label1.config(text=str(counter))
    
button = tkinter.Button(window, text='this is temp button', command=temp)
button.pack()

scale = tkinter.Scale(window, variable=var, orient='horizontal'
                      , tickinterval=50, to=500, length=300, command=temp)

scale.pack()

label = tkinter.Label(window, text='value: 0')
label.pack()

label1 = tkinter.Label(window, text = 'num: ')
label1.pack(side='right')

window.mainloop()