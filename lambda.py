import basic
import tkinter as tk

window = basic.window_setup().window
window.title('this is a lambda function practice')

def command_args(first, second, third):
    global arg1
    arg1 = first * 2
    print(first, second, third)
    
# 이렇게 parameter가 있는 함수를 command에 쓰려면 lambda를 사용해야 함
    
arg1 = 1
arg2 = 'alpha'
arg3 = 'beta'

b = tk.Button(window, width=30, height=15,
              text='click it', command=lambda: command_args(arg1, arg2, arg3))
b.pack(expand=True, anchor='center')

window.mainloop()