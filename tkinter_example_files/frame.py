import tkinter

window = tkinter.Tk() 

window.title("this is frame practice")
window.resizable(True, True)
window.geometry("400x400+100+100")
# bg는 background color, bd는 프레임의 테두리 두께를 지정
frame1 = tkinter.Frame(window, relief='solid', bd=2)
frame1.pack(side='left', fill='both', expand=False)

frame2 = tkinter.Frame(window, relief='solid', bd=2)
frame2.pack(side='right', fill='both', expand=False)

button1 = tkinter.Button(frame1, text='first frame') # 버튼은 프레임 내에 배치 가능
button2 = tkinter.Button(frame2, text='second frame')
button1.pack(anchor='center')
button2.pack(anchor='center', side='left')

frame3 = tkinter.Frame(window, relief='solid', bd=2)
frame3.pack(side='bottom', fill='both', expand=False)

window.mainloop()