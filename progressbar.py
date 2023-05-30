import basic
import tkinter.ttk

window = basic.window_setup().window
window.title('this is a progressbar practice')

progress_bar = tkinter.ttk.Progressbar(window,
                                       maximum=200, mode='determinate', length=400,
                                       orient='horizontal')
# mode는 표시 스타일
# 
progress_bar.pack()

#progress_bar.start(100) # progressbar가 지정된 숫자의 밀리초마다 움직임

label = tkinter.Label(window, text='in progress')
label.pack()

process = 0
def update(): # []의 형식으로 각 위젯의 속성 value들을 중간에 변경할 수 있음
    global process
    process += 1
    progress_bar['value'] = process
    if progress_bar['value'] == progress_bar['maximum'] - 1:
        label.config(text='process complete')
        progress_bar.stop()
        return
    window.after(1000, update) # 매 1000 밀리초마다 update가 실행됨; 
                            # 지정된 값에 도달하면 return

update()
window.mainloop()