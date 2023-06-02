import tkinter

window = tkinter.Tk()

window.title("this is listbox practice")
window.resizable(True, True)
window.geometry("400x400+100+100")

CheckVariety_1 = tkinter.IntVar()
CheckVariety_2 = tkinter.IntVar()
CheckVariety_3 = tkinter.IntVar()

def summation_in_the_future():
    for i in range(2):
        checkbutton1.flash()
checkbutton1 = tkinter.Checkbutton(window, 
                                   text = "I want summation",
                                   activebackground="slate gray",
                                   command=summation_in_the_future,
                                   variable=CheckVariety_1)
checkbutton2 = tkinter.Checkbutton(window,
                                   text = "I want multiplication",
                                   activebackground="slate grey",
                                   variable=CheckVariety_2
                                   )
checkbutton3 = tkinter.Checkbutton(window,
                                   text="I want both",
                                   activebackground="slate grey",
                                   variable=CheckVariety_3)
checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

window.mainloop()