import tkinter

window = tkinter.Tk() # grid 랑 pack은 동시에 사용할 수 없음

window.title("this is menu practice")
window.resizable(True, True)
window.geometry("400x400+100+100")

b1 = tkinter.Button(window, text='top')
b1_1 = tkinter.Button(window, text='top - 1')

b2 = tkinter.Button(window, text='bottom')
b2_2 = tkinter.Button(window, text='bottom - 1')

b3 = tkinter.Button(window, text='left')
b3_3 = tkinter.Button(window, text='left - 1')

b4 = tkinter.Button(window, text='right')
b4_4 = tkinter.Button(window, text='right - 1')

b5 = tkinter.Button(window, text='center', bg='red')

b1.pack(side='top')
b1_1.pack(side='top', fill='x') # fill은 할당된 공간에 대한 크기 맞춤

b2.pack(side='bottom')
b2_2.pack(side='bottom', anchor='w') # anchor는 정해진 공잔 내에서의 동서남북중 위치 지정

b3.pack(side='left')
b3_3.pack(side='left', fill='y')

b4.pack(side='right')
b4_4.pack(side='right', fill='y')

b5.pack(expand=True, fill='both') # fill이 both면 x,y 두 방향으로 맞춰짐
# 여기서 expand는 모든 미사용 공간을 점유 및 사용함



window.mainloop()