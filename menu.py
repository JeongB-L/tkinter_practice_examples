import tkinter

window = tkinter.Tk()

window.title("this is menu practice")
window.resizable(True, True)
window.geometry("400x400+100+100")
def close():
    window.quit()
    window.destroy() # destroys all widgets
    
# menu 자체가 top level 윈도우로 취급됨
menubar = tkinter.Menu(window) # menu를 생성함; 이거 자체로는 보이는건 없음

menu_1 = tkinter.Menu(window, tearoff=0) # tearoff 값은 첫 번째 하위 메뉴가 위에서부터
                                         # 얼마나 아래로 갈지 지정할 수 있음
menu_1.add_command(label='lower menu 1-1')
menu_1.add_command(label='lower menu 1-2')
menu_1.add_separator() # 하위 메뉴 내에서 separator를 추가함; 위, 아래를 나누는 선
menu_1.add_command(label='lower menu 1-3', command=close)
menubar.add_cascade(label='upper menu 1', menu=menu_1) # 생성된 menu(menubar)을 
 
 # radiobuttton은 한번에 무조건 하나만 체크 가능
menu_2 = tkinter.Menu(window, tearoff=0, selectcolor="red") # selectcolor을 해서 체크표시의 색을 결정
menu_2.add_radiobutton(label='lower menu 2-1', state="disable") # state literally is state
menu_2.add_radiobutton(label='lower menu 2-2')
menu_2.add_radiobutton(label='lower menu 2-3')
menubar.add_cascade(label='upper menu 2', menu=menu_2)


#checkbox는 한번에 여러개 체크 가능
menu_3 = tkinter.Menu(window, tearoff=20, selectcolor='blue')
menu_3.add_checkbutton(label='close', command=close)
menu_3.add_checkbutton(label='lower menu 3-2')
menubar.add_cascade(label='upper menu 3', menu=menu_3)

window.config(menu=menubar)

window.mainloop()