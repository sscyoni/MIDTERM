class DSstudent :
  def __init__(self,stu_id,name) :
    self.stu_id = stu_id
    self.name =name

  def show_info(self) :
    print("학번:",self.stu_id,",", "이름:",self.name)

class UndergraduateStudent(DSstudent) :
  def __init__(self,major) :
    self.major = major
  def introduce (self) :
    print (f"저는 학부생 {self.name},저의 전공은 {self.major}")


class GraduateStudent(DSstudent) :
  def __init__(self,advisor) :
    self.advisor = advisor
  def introduce (self) :
    print (f"저는 대학원생 {self.name},지도교수는 {self.advisor}")





aa = DSstudent(20251335,"신채연")
aa.show_info()

stu1= UndergraduateStudent("202501","김민수","컴퓨터공학과")
stu2 = GraduateStudent("202401","이수정","홍길동")

stu1.show_info()
stu1.introduce()
stu2.show_info()
stu2.introduce()