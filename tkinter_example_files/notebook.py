import basic
import tkinter
import tkinter.ttk

window = basic.window_setup().window
window.title('this is a notebook practice')
# canvas랑은 다름
# frame에 notebook을 넣을 수도 있고 그 반대도 가능

# 페이지를 frame으로 나눌 수 있는 탭 메뉴 생성

notebook = tkinter.ttk.Notebook(window, width=300, height=300)
notebook.pack()

frame1 = tkinter.Frame(window)
notebook.add(frame1, text='page 1')

l1 = tkinter.Label(frame1, text='content of page1')
l1.pack()

frame2 = tkinter.Frame(window)
notebook.add(frame2, text='page 2')

l2 = tkinter.Label(frame2, text='content of page2')
l2.pack()

frame4 = tkinter.Frame(window)
notebook.add(frame4, text='page 4')

l4 = tkinter.Label(frame4, text='content of page4')
l4.pack()

frame3 = tkinter.Frame(window)
notebook.insert(1, frame3, text='page 3')
# insert는 탭 메뉴에서 지정된 index 위치에 해당 frame 또는
# whatever that comes를 추가함

l3 = tkinter.Label(frame3, text='content of page3')
l3.pack()
window.mainloop()