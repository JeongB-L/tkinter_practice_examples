import basic
import tkinter

window = basic.window_setup().window
window.title('scrollbar practice for horizontal scrollbar')

frame = tkinter.Frame(window)

scrollbar = tkinter.Scrollbar(frame)


scrollbar.pack(side='right', fill='y')

listbox = tkinter.Listbox(frame, yscrollcommand=scrollbar.set)

for temp in range(100):
    listbox.insert(temp, str(temp) + f'hoho {temp}')
    
listbox.pack(side='left')

scrollbar['command'] = listbox.yview

frame.pack()

window.mainloop()