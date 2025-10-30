from tkinter import*

root = Tk()
root.title ("중간고사 7번")
root.geometry("420x440")

canvas = Canvas(root,width=400,height=320,bg= "white")
canvas.pack()


def aa () :
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 50, 50, fill="red")

def bb () :
    canvas.delete("all")
    canvas.create_oval(100, 100, 200, 200, fill="blue")

def cc() :
    canvas.delete("all")
    global img
    img = PhotoImage(file = "C:\Users\DS\Pictures\빵.jpg")
    canvas . create_image(100,50,anchor = NW,image = img)

def dd() :
    canvas.delete("all")

frame = Frame(root,width=200,height=100)
frame.pack()

but1 = Button(frame,text='사각형', command = aa)
but1.pack()
but2 = Button(frame,text='원', command = bb)
but2.pack()

but3 = Button(frame,text='그림', command = cc)
but3.pack()
but4 = Button(frame,text='지우기', command = dd)
but4.pack()

lb1 = Label(root,"버튼을 눌러 도형을 선택하세요.").pack()


root.mainloop()