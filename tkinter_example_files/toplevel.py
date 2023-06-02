import basic
import tkinter as tk

window = basic.window_setup().window
window.title('toplevel practice window')

# 다른 위젯들을 포함하는 외부 윈도우
# 다른 위젯들, 예를 들어 메뉴를 기본 윈도우에 추가한 후 추가 윈도우에만 display를 하도록 
# 할 수 있음

menubar = tk.Menu(window)

menu_1 = tk.Menu(menubar, tearoff=0)
menu_1.add_command(label='lower_menu 1-1')
menu_1.add_command(label='lower_menu 1-2')
menu_1.add_separator()
menu_1.add_command(label='lower_menu 1-3')
menubar.add_cascade(label='upper menu 1', menu=menu_1)

menu_11 = tk.Menu(menu_1, tearoff=0)
menu_11.add_command(label='sub menu 1-1')
menu_11.add_separator()
menu_11.add_checkbutton(label='this is the one')
menu_1.add_cascade(label='lower_menu 1-4', menu=menu_11)

toplevel = tk.Toplevel(window, menu=menubar)
toplevel.title('this is a toplevel sub window')
toplevel.resizable(False, False)

def close(event):
    toplevel.withdraw()
    window.quit()
    window.destroy()
    
toplevel.bind('<Button-1>', close)
toplevel.geometry("320x200+820+200")

label = tk.Label(toplevel, text='jeongbin lee')
label.pack()
label2 = tk.Label(window, text='hohohoho')
label2.pack()

window.mainloop()