from pymongo import MongoClient
import tkinter

import datetime
import os
from bson import ObjectId
import pprint
MONGODB_URI = "mongodb+srv://admin:admin@cluster0.hbr4h1g.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URI)
db = client.blog

current_collection = db.posts

window = tkinter.Tk() # 가장 상위 레벨의 윈도우 창

window.title('temporary window')
window.geometry("400x400+100+100") # 너비 높이 x좌표 y좌표
window.resizable(True, True) # 상하, 좌우

#window.mainloop() # 윈도우가 종료될 때 까지 실행될 수 있도록 함
# 또한 윈도우 자체를 시작함
label = tkinter.Label(window, text = "hello world")
label2 = tkinter.Label(window, text = "how does this work now?")
label.pack() # 해당 위젯을 배치함, 기본적으로 위에서 아래로 하나하나씩 추가됨
label2.pack() 

label3 = tkinter.Label(window, text="python here", anchor = "ne", width = 30, height = 30, fg="blue", relief="solid")
label3.pack()
window.mainloop()