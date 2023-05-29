import basic
import tkinter

window = basic.window_setup().window
window.title('text practice for text')

# text는 string print를 위한 위젯

sb = tkinter.Scrollbar(window, orient='vertical')
sb.pack(side='right', fill='y')

text = tkinter.Text(window, yscrollcommand=sb.set)

text.insert(tkinter.CURRENT, "hello world.\n")
text.insert("current", "반습니다.")
text.insert(2.1, '갑') # 2.1은 두 번쨰 줄의 1 번쨰 col; 0부터 카운팅 시작

for _ in range(100):
    text.insert('current', 'omomo\n')
sb.config(command=text.yview)

text.pack()

text.tag_add('emphasis', '1.0', '1.6') 
text.tag_config('emphasis', background='yellow')
text.tag_remove('emphasis', '1.1', '1.2')
 
window.mainloop()