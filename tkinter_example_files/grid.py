import tkinter

window = tkinter.Tk() # grid 랑 pack은 동시에 사용할 수 없음

window.title("this is grid practice")
window.resizable(True, True)
window.geometry("400x400+100+100")

# grid는 셀 단위로 배치; pack과 마찬가지로 즉각적으로 배치하며 
# pack이랑은 다름

# 다만 셀을 건너뛸 수는 없음

b1=tkinter.Button(window, text="(0, 0)")
b2=tkinter.Button(window, text="(0, 1)", width=20)
b3=tkinter.Button(window, text="(0, 2)")

b4=tkinter.Button(window, text="(1, 0)")
b5=tkinter.Button(window, text="(1, 1)")
b6=tkinter.Button(window, text="(1, 3)")

b7=tkinter.Button(window, text="(2, 1)")
b8=tkinter.Button(window, text="(2, 2)")
b9=tkinter.Button(window, text="(2, 4)")

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0, rowspan=2)
b5.grid(row=1, column=1, columnspan=3, rowspan=2)
b6.grid(row=1, column=3)

b7.grid(row=2, column=1, sticky="w")
b8.grid(row=2, column=2)
b9.grid(row=2, column=99)
# place는 절대적인 위치이며 이는 resizable의 영향을 받아서 위치됨
p1 = tkinter.Button(window, text='placed').place(x=150, y=50, width=50,
                                                 height=20, bordermode='inside',
                                                 relx=0.5)
# relx는 x 또는 y 좌표의 배치 비율

window.mainloop()