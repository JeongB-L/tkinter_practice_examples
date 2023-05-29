import tkinter

window = tkinter.Tk()

window.title("this is menu practice")
window.resizable(True, True)
window.geometry("400x400+100+100")
# 메뉴버튼은 메뉴 기능을 가진 버튼을 생성
menubutton = tkinter.Menubutton(window, text='menu menu button', 
                                relief='raised', direction='right')
menubutton.pack() # relief는 해당 버튼의 3d 효과를 설정하는 값

def close():
    window.quit()
    window.destroy()

menu = tkinter.Menu(menubutton, tearoff=0) # 윈도우가 아닌 menubutton 자체를 메뉴로 설정

menu.add_command(label='lower menu 1', command=close)
menu.add_separator()
menu.add_command(label='lower menu 2')

menubutton["menu"]=menu


window.mainloop()
