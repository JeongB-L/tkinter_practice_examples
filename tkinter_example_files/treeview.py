import basic
import tkinter
import tkinter.ttk

window = basic.window_setup.window
window.title('treeview')

treeview = tkinter.ttk.Treeview(window,
                                columns=['one', 'two'],
                                displaycolumns=['two','one'])
# column과 보여질 column의 갯수: one two 이렇게 있으면 one이라는 
# column과 two라는 column이 생성되어 총 2개의 기둥이 생성됨
# 기본 왼쪽의 column인 0도 있음; 결과적으로는 3개
treeview.pack()

def callback(self):
    treeview.tag_configure('tag2', background='red')

treeview.column('#0', width=70) # 0번째 인덱스 column 조정
treeview.heading('#0', text='num') # heading은 내용 조정, column은 위치 조정

treeview.column('one', width=100, anchor='center')
treeview.heading('one', text='letter', anchor='e')

treeview.column('#2', width=100, anchor='w')
treeview.heading('two', text='ASCII', anchor='center')

treelist=[("A", 65), ("B", 66), ("C", 67), ("D", 68), ("E", 69)]

for i in range(len(treelist)):
    treeview.insert('', 'end', text=i + 1, values=treelist[i], iid=str(i) + '번')
    # 튜플을 받았기에 두 값들을 각 row에 채워넣음

top = treeview.insert('', 'end', text=str(len(treelist)), iid='5번', tags='tag1')

top_mid1=treeview.insert(top, 'end', text="5-2", values=["what", 1], iid="5번-1")
top_mid2=treeview.insert(top, 0, text="5-1", values=["is", 0], 
                         iid="5번-0", tags="tag2")
top_mid3=treeview.insert(top, 'end', text="5-3", values=["this", 2], 
                         iid="5번-2", tags="tag2")

treeview.tag_bind('tag1', sequence='<<TreeviewSelect>>', callback=callback)
window.mainloop()