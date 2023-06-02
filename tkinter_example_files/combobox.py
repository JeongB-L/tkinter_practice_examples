import basic
import tkinter as tk
import tkinter.ttk

window = basic.window_setup().window
window.title('comboBox practice window')
values = [str(i) + '번' for i in range(1, 101)]
values.append('finale')

combobox = tkinter.ttk.Combobox(window, height=15, value=values)
combobox.pack()

combobox.set('목록 선택')
window.mainloop()

# 주어진 값들의 리스트 중에서 하나를 선택하게 할 수 있는 박스를 생성