import basic
import tkinter as tk
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://admin:admin@cluster0.hbr4h1g.mongodb.net/"
client = MongoClient(MONGODB_URI)
db = client.blog
crr_collection = db.comments

first_stage = {'$match': {"title": "The Favourite"}}
second_stage = {'$project': {'title': 1, 'year': 1, '_id': 0}}

pipeline = [first_stage, second_stage]

result = crr_collection.aggregate(pipeline=pipeline)
temp = []
for i in result:
    temp.append(i)

window = basic.window_setup().window
window.title('labelframe practice window')

# 다른 위젯들을 포함하고 구역을 나눌 수 있는 내부적인 윈도우를 생성
# frame이나 labelframe처럼 그냥 영역만 나누는것은 아님

subwindow1 = tk.PanedWindow(relief='raised', bd=2)
subwindow1.pack(expand=True)
# labelFrame처럼 내용물이 있어야 display됨

left = tk.Label(subwindow1, text='internal window - 1 left') # 순서대로 왼쪽 추가, 중앙 추가, 우측 추가
subwindow1.add(left)

subwindow1_1 = tk.PanedWindow(relief='groove', orient='vertical', bd=3)
subwindow1.add(subwindow1_1)

right = tk.Label(subwindow1, text='internal window - 2 right')
subwindow1.add(right)

# 오른쪽까지 다 추가했으니 이제 다시 중앙에서 fill out

#top = tk.Label(subwindow1_1, text='internal window - 3 upper')
top = tk.Label(subwindow1_1, text=temp[0])
subwindow1_1.add(top)

bottom = tk.Label(subwindow1_1, text='internal window - 4 lower')
subwindow1_1.add(bottom)


window.mainloop()