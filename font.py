import basic
import tkinter as tk
from tkinter import font

window = basic.window_setup().window
window.title('this is font practice')

font = tk.font.Font(family='Calibri', size=20, slant='italic')

label = tk.Label(window, text='이것은 맑은 고딕heoeh', font=font)
label.pack()

window.mainloop()