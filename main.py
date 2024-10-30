import tkinter as tk
import random as r
# tạo đối tượng cửa sổ
root=tk.Tk()
# tạo kích thước + vị  trí cửa  sổ
root.geometry('1000x700+500+50')
# đổi màu nền sau khi tạo cửa sổ
root.configure(bg='navy')
# đặt tiêu đề
root.title('Lesson 3')
# đổi icon cửa sổ
root.iconbitmap('HINH/images.ico')
# tạo label
# đặt  vị trí
# đổi màu nền label
# đặt nội dung label và trang trí
def creat_label():
    label= tk.Label(root,bg='lightblue',text='Grim reaper',relief='raised',font=('Arial', 12,'italic bold'), bd=5,fg='black',width=30,height=500,anchor='center')
    label.pack(side='top',fill='y',expand='False')
    return label


def Upadte_text(label):
    texts=['Python is great','hello world','hello Tkinter','Tkinter is great']
    new_texts=r.choice(texts)
    label.configure(text=new_texts)
    root.after(1000,Upadte_text,label)


def update_place(label):
    xs=0
    xe=900
    ys=0
    ye=600
    new=r.randint()

label=creat_label()
Upadte_text(label)

root.mainloop()