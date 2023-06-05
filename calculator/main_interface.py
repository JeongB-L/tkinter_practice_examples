import tkinter as tk
import tkinter.ttk as tki
import key_functions as kf
import tkinter.font as tkf
import settings


class main_gui(object):
    settings.init()
    
    root = tk.Tk()
    root.title('calculator')
    root.geometry("452x500+790+270")
    root.resizable(False, False)

    # add two frames for top and left
    left_frame = tk.Frame(root, relief='solid', bd=1)
    left_frame.grid(row=4, column=0)

    # add buttons: 1 2 3 4 5 6 7 8 9 0 C () % / X - + . = backspace
    b_num_1 = tk.Button(left_frame, text='1',
                        width=5, height=3, bd=2,
                        command=kf.one_is_pressed)
    b_num_1.grid(row=0, column=0)

    b_num_2 = tk.Button(left_frame, text='2',
                        width=5, height=3, bd=2,
                        command=kf.two_is_pressed)
    b_num_2.grid(row=1, column=0)

    b_num_3 = tk.Button(left_frame, text='3',
                        width=5, height=3, bd=2,
                        command=kf.three_is_pressed)
    b_num_3.grid(row=2, column=0)

    b_num_4 = tk.Button(left_frame, text='4',
                        width=5, height=3, bd=2,
                        command=kf.four_is_pressed)
    b_num_4.grid(row=3, column=0)

    b_num_5 = tk.Button(left_frame, text='5',
                        width=5, height=3, bd=2,
                        command=kf.five_is_pressed)
    b_num_5.grid(row=4, column=0)

    b_num_6 = tk.Button(left_frame, text='6',
                        width=5, height=3, bd=2,
                        command=kf.six_is_pressed)
    b_num_6.grid(row=5, column=0)

    b_num_7 = tk.Button(left_frame, text='7',
                        width=5, height=3, bd=2,
                        command=kf.seven_is_pressed)
    b_num_7.grid(row=6, column=0)

    b_num_8 = tk.Button(left_frame, text='8',
                        width=5, height=3, bd=2,
                        command=kf.eight_is_pressed)
    b_num_8.grid(row=7, column=0)

    b_num_9 = tk.Button(left_frame, text='9',
                        width=5, height=3, bd=2,
                        command=kf.nine_is_pressed)
    b_num_9.grid(row=8, column=0)

    b_num_0 = tk.Button(left_frame, text='0',
                        width=5, height=3, bd=2,
                        command=kf.zero_is_pressed)
    b_num_0.grid(row=0, column=1)

    b_num_C = tk.Button(left_frame, text='C',
                        width=5, height=3, bd=2,
                        command=kf.C_is_pressed)
    b_num_C.grid(row=1, column=1)
    
    # % mod
    b_num_mod = tk.Button(left_frame, text='mod',
                          width=5, height=3, bd=2,
                          command=kf.mod_is_pressed)
    b_num_mod.grid(row=2, column=1)
    # / division
    b_num_div = tk.Button(left_frame ,text='div',
                          width=5, height=3, bd=2,
                          command=kf.division_is_pressed)
    b_num_div.grid(row=3, column=1)
    # x multiplication
    # + addition
    # - subtraction
    # . point
    # del delete
    # ( left bracket
    # ) right bracket
    # = equal sign

    # bind each button with their respective keys
    # and functions
    # ex) root.bind('c', press)
    root.bind('1', kf.one_is_pressed)
    root.bind('2', kf.two_is_pressed)
    root.bind('3', kf.three_is_pressed)
    root.bind('4', kf.four_is_pressed)
    root.bind('5', kf.five_is_pressed)
    root.bind('6', kf.six_is_pressed)
    root.bind('7', kf.seven_is_pressed)
    root.bind('8', kf.eight_is_pressed)
    root.bind('9', kf.nine_is_pressed)
    root.bind('0', kf.zero_is_pressed)
    root.bind('c', kf.C_is_pressed)
    
    # as numerics are typed, make them visible on GUI
        
    answer_font = tkf.Font(family='Times', size=30)
    settings.answer = tk.Label(root, font=answer_font, width=15, height=8, bd=3,
                      relief='solid', text='hi')
    
    settings.answer.grid(row=4, column=3)
    
    # process the equation whenever = is clicked


if __name__ == "__main__":
    main_gui.root.mainloop()
