import tkinter

window = tkinter.Tk()

window.title("this is listbox practice")
window.resizable(True, True)
window.geometry("400x400+100+100")

scrollbar1 = tkinter.Scrollbar(window)
scrollbar1.pack(side="right", fill="y")

listbox = tkinter.Listbox(window, selectmode='extended', height=0, width=20, relief="groove",
                          borderwidth=5, background="blue", yscrollcommand=scrollbar1.set)
listbox.insert(0, "td]wo")
listbox.insert(1, "td]wo")
listbox.insert(2, "td]wo")
listbox.insert(3, "td]wo")
listbox.insert(4, "td]wo")
listbox.insert(5, "td]wo")
listbox.delete(0, 1)

listbox.pack()
window.mainloop()
