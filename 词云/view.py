from tkinter import *
import main
import webbrowser
from tkinter import messagebox
def made(oid,path):
    
    main.get_ciyun(oid,path)
def open():
    webbrowser.open_new("https://space.bilibili.com/247987609?spm_id_from=333.1007.0.0")
def open2():
    webbrowser.open_new("https://zhangyizhang.top/pages/bilibili词云")
def open3():
    messagebox.showinfo('声明','本作品由爱写代码的老张制作，且本作品遵循gpl协议开源')
root= Tk()
root.title('bilibili词云生成')
root.geometry('380x190') # 这里的乘号不是 * ，而是小写英文字母 x
root.resizable(width=False, height=False)
#________________________________
L1 = Label(root,text="视频bid")
L1.grid(row=0,column=0)
oid = Entry(root,bd=5,width=40)
oid.grid(row=0,column=1)
oid.insert(0, "BV13A411C74j")
#________________________________
L5 = Label(root,text="存放路径")
L5.grid(row=4,column=0)
path = Entry(root,bd=5,width=40)
path.grid(row=4,column=1)
path.insert(0, "C:\\词云.png")
#________________________________
b1 = Button(root,text="制作词云",command=lambda:made(oid.get(),path.get()),bd=5, width=6, height=1)
b1.grid(row=5,column=0)
#________________________________
b2 = Button(root,text="作者主页",command=lambda:open(),bd=5, width=6, height=1)
b2.grid(row=5,column=1)
#________________________________
b3 = Button(root,text="源代码",command=lambda:open2(),bd=5, width=6, height=1)
b3.grid(row=6,column=0)
#________________________________
b4 = Button(root,text="声明",command=lambda:open3(),bd=5, width=6, height=1)
b4.grid(row=6,column=1)
#________________________________
root.mainloop()