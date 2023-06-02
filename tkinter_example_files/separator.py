import tkinter
import tkinter.ttk

window = tkinter.Tk()
window.title('separator practice')
window.geometry("640x480+100+100")
window.resizable(False, False)
# sepeartor 자체를 그리는 법
b1 = tkinter.Button(window, width=10, height=5, text='one')
b1.grid(row=0, column=0)
b2 = tkinter.Button(window, width=10, height=5, text='two')
b2.grid(row=0, column=2)
b3 = tkinter.Button(window, width=10, height=5, text='three')
b3.grid(row=1, column=1)
b4 = tkinter.Button(window, width=10, height=5, text='four')
b4.grid(row=2, column=0)
b5 = tkinter.Button(window, width=10, height=5, text='five', relief='solid')
b5.grid(row=2, column=2)

s1 = tkinter.ttk.Separator(window, orient='vertical')
s1.grid(row=0, column=1, sticky='ns') # vertical => ns, horizontal => ew 무조건
s2 = tkinter.ttk.Separator(window, orient='horizontal')
s2.grid(row=1, column=0, sticky='ew')
s3 = tkinter.ttk.Separator(window, orient='vertical')
s3.grid(row=1,column=0, sticky='ns')


window.mainloop()