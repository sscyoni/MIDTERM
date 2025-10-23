from tkinter import *
root = Tk()
root.geometry("250x150")
root.title("중간고사 5번")

class Student :
  def __init__(self,stu_id,name) :
    self.stu_id = stu_id
    self.name =name
    
  def __eq__ (self,other) :
      if isinstance(other,User) :
          return self.name == other.name
      return False
  
students = [Student("202501","김민수"),Student("202502","이수정"),Student("202503","박지훈")]
  
lab1 = Label(root,text="학번").grid(row=0)

lab2 = Label(root,text="이름").grid(row=1)


ent1 = Entry (root)
ent1.grid(row=0,column=1)
ent2 = Entry (root)
ent2.grid(row=1,column=1)

def aa () :
    print("로그인성공")
    
btn1 = Button(root)
btn1.config(text="로그인",command = aa)
btn1.grid(row=3,column=0)

btn2 = Button(root)
btn2.config(text="취소",command = root.quit)
btn2.grid(row=3,column=1)

root.mainloop()


