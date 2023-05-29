import tkinter

window = tkinter.Tk()

window.title("this is radiobutton practice")
window.resizable(True, True)
window.geometry("400x400+100+100")

RadioVariety_1 = tkinter.IntVar()
RadioVariety_2 = tkinter.IntVar()
# 라디오버튼은 일종의 원 모양의 체크박스

def check():
    # 빈 label에다가 function할 것을 추가
    label.config(text= "RadioVariety_1 = " + str(RadioVariety_1.get()) + "\n" +
                       "RadioVariety_2 = " + str(RadioVariety_2.get()) + "\n\n" +
                       "Total = "          + str(RadioVariety_1.get() + RadioVariety_2.get()))

radio1=tkinter.Radiobutton(window, text="1번", value=3, variable=RadioVariety_1, command=check)
radio1.pack()
# value는 해당 버튼이 눌렸을 때 할당되는 값
radio2=tkinter.Radiobutton(window, text="2번(1번)", value=3, variable=RadioVariety_1, command=check)
radio2.pack()

radio3=tkinter.Radiobutton(window, text="3번", value=9, variable=RadioVariety_1, command=check)
radio3.pack()

label=tkinter.Label(window, text="None", height=5)
label.pack()

radio4=tkinter.Radiobutton(window, text="4번", value=12, variable=RadioVariety_2, command=check)
radio4.pack()

radio5=tkinter.Radiobutton(window, text="5번", value=15, variable=RadioVariety_2, command=check)
radio5.pack()
window.mainloop()