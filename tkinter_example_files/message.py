import tkinter
import basic

basicvar = basic.var1
print(basicvar)

window = basic.window_setup.window

message = tkinter.Message(window, text='this is message', width=100, relief='flat')
message.pack(side='left', anchor='e', fill='x')

window.mainloop()



