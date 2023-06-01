import cv2
import tkinter
from PIL import Image
from PIL import ImageTk


window=tkinter.Tk()
window.title("this is opencv application")
window.geometry("640x480+100+100")
window.resizable(True, True)

source = cv2.imread('박지옷.PNG')
try:
    source = cv2.resize(source, (640, 400))
except:
    print('error?')

def convert_to_tkimage():
    global source
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    #_, 는 그 값을 무시하기 위해 지정; 
    # cv2.threshold에서 값이 a b 이렇게 나오면 b만 사용하고 a는 무시
    img = Image.fromarray(binary)
    imgtk = ImageTk.PhotoImage(image=img)
    label.config(image=imgtk)
    label.image=imgtk


img = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)

img = Image.fromarray(img)

imgtk = ImageTk.PhotoImage(image=img)

label = tkinter.Label(window, image=imgtk)
label.pack(side='top')

button = tkinter.Button(window, text='made in binary', command=convert_to_tkimage)
button.pack(side='buttom', expand=True, fill='both')

window.mainloop()