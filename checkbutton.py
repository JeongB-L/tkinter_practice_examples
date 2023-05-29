import tkinter

window = tkinter.Tk()

window.title("this is listbox practice")
window.resizable(True, True)
window.geometry("400x400+100+100")

def command_in_use():
    checkbutton_1.flash()
    #다만 command는 공유되는 것이 아니라
    # 지정된 버튼에 의해서만 실행됨 

CheckVariety_1 = tkinter.IntVar()
CheckVariety_2 = tkinter.IntVar()
# intVar는 tkinter의 상태를 제어하는 변수
# 체크가 되었나 안되었나를 저장함

checkbutton_1 = tkinter.Checkbutton(window, text="O",
                                    variable = CheckVariety_1,
                                    activebackground="blue")
checkbutton_2 = tkinter.Checkbutton(window, text="△",
                                    variable = CheckVariety_2,
                                    activebackground="red")
checkbutton_3 = tkinter.Checkbutton(window, variable=CheckVariety_2,
                                    command=command_in_use, 
                                    activebackground="red")
# 같은 checkvariaty variable을 사용하면 같은 status가 됨

checkbutton_1.pack()
checkbutton_2.pack()
checkbutton_3.pack()

window.mainloop()