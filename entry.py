import tkinter
from math import *

window = tkinter.Tk()

window.title("qthis is entry practice")
window.resizable(True, True)
window.geometry("400x400+100+100")

# entry는 입력 및 출력을 위한 작은 창을 생성할 수 있도록 함

def quickCalc(event):
    label.config(text="The result of your calculation is "+str(eval(entry.get()))) #entry.get으로 받은 
    # 수식의 값을 label에 출력. eval은 math function
    temp.config(text='hahe')

entry = tkinter.Entry(window) # entry 창의 속성 설정
entry.bind("<Return>", quickCalc) # sequence to call functions; fucntion 실행
# Return이 눌려지면 quickCalc funciton을 실행함
entry.pack()

label = tkinter.Label(window)
label.pack()

temp = tkinter.Label(window)
temp.pack()

window.mainloop()