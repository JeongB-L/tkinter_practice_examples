import basic
import tkinter

window = basic.window_setup().window
window.title('labelframe practice window')

# label frame은 다른 위젯들을 포함함과 동시에 캡션을 가지는 프레임
# 사각형 위쪽에 캡션이라 부르는 텍스트를 넣을 수 있음

labelFrame = tkinter.LabelFrame(window, text='select your platform')
labelFrame.pack()
# labelframe 자체만으로는 아무것도 표시되지 않기에 안에 뭐가 있어야됨

def check():
    label.config(text=RadioVariety1.get()) # label에 radiovariety1에 저장된 값을 불러옴

RadioVariety1 = tkinter.StringVar()
RadioVariety1.set("yet to be selected")

radio1 = tkinter.Radiobutton(labelFrame, text='python', value='yes', variable=RadioVariety1, command=check)
radio1.pack()

radio2 = tkinter.Radiobutton(labelFrame, text='C/C++', value='ehh', variable=RadioVariety1,
                             command=check)
radio2.pack()

radio3 = tkinter.Radiobutton(labelFrame, text='Java', value='no', variable=RadioVariety1,
                             command=check)
radio3.pack()

radio3 = tkinter.Radiobutton(labelFrame, )
label = tkinter.Label(labelFrame, text='None')
label.pack()
window.mainloop()