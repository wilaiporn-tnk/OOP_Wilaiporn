class Animal:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
    def showinfo(self):
        return f"ชื่อ {self.name} อายุ {self.age} ปี มีสี {self.color}"
#animal = Animal ('ปีเตอร์' , 'ดำ')
#print(f"สัตว์ตัวหนึ่งมี(animal.showinfo()))
class Dog:
    def spak(self):
        return "โฮ่งๆๆ"
dog1 = Dog ('ปีเตอร์','ดำ')
print(f"หมาชื่อ {dog1.name} ร้อง {dog1.speak()}")
print(f"ข้อมูลหมาคัวที่ 1 คือ {dog1.showinfo()}")

 
        