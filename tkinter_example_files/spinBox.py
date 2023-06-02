import basic
import tkinter as tk

window = basic.window_setup().window
window.title('spinbox practice window')

label = tk.Label(window, text='please enter a number', height=3)
label.pack()

def value_check(temp):
    label.config(text='please enter a number')
    valid = False
    if temp.isdigit():
        if int(temp) <= 50 and int(temp) >= 0:
            valid = True
            label.config(text=str(temp) + ' is your answer')
    elif temp == '':
        valid = True
    return valid

# 위아래로 값을 올리고 내릴 수도 있는 entry box를 생성

def value_error(temp):
    label.config(text=str(temp) + ' is your answer. \n Please enter a valid number')
    
validate_command = (window.register(value_check), '%P')
invalid_command = (window.register(value_error), '%P')

spinbox = tk.Spinbox(window, from_= 0, to = 50, validate='all',
                     validatecommand=validate_command, 
                     invalidcommand=invalid_command,
                     relief='solid', bd=3, bg='blue', fg='pink',
                     insertwidth=3, insertborderwidth=3)
# 여기서 from and to는 그 값들 사이만 입력 가능하게 하는것

spinbox.pack(expand=True)
    

window.mainloop()