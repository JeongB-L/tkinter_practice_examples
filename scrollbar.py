import basic
import tkinter

window = basic.window_setup().window
window.title('this is a scrollbar practice')

# 위젯에 적용하기 위한 스크롤바 생성
frame = tkinter.Frame(window)
scrollbar = tkinter.Scrollbar(frame, orient='vertical')

scrollbar.pack(side='right', fill='y')

listbox = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)
for index in range(1, 1001):
    listbox.insert(index, str(index) + "/1000")
listbox.pack(side='left')

scrollbar['command'] = listbox.yview # 여기서 command를 사용하여 적용될 위젯과 연결
# 여기서 command는 scrollbar의 parameter 중 하나로서 []을 사용하여 나중에 추가적으로 등록이 가능
# 우선 command만 이렇게 따로 추가적인 등록이 가능함
# yview()가 아니라 yview가 필요함. ()가 없으면 그냥 class variable


frame.pack()
window.mainloop()