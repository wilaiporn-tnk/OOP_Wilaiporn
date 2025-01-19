class Product:
    def __init__(self,brand,name,price,stock):
        self.brand = brand
        self.name = name
        self.__price = price
        self.__stock = stock

    def edit(self,val):
        if val == "editstock" :
            print('แก้ไขจำนวน')
            val_stock = int(input(f'{self.brand} ใส่จำนวน : '))
            self.__stock += val_stock
        
        elif val == "editprice":
            print('แก้ไขราคา')
            val_price = int(input(f'{self.brand} ใส่ราคา : '))
            self.__price = val_price

    def showinfo(self):
        return f"ชื่อแบรด์สินค้า: {self.brand} สินค้าชื่อ: {self.name} ราคา: {self.__price} บาท มีจำนวน: {self.__stock} ชิ้น"
    
class Mobile(Product):
    def __init__(self,brand, name, price, stock,system):
        super().__init__(brand,name, price, stock)
        self.system = system
    def showmobile(self):
        return f"{super().showinfo()}\nระบบปฏิบัติการ : {self.system}\n--------------------------------------------------------------------------------------"
    
class Notebook(Product):
    def __init__(self,brand, name, price, stock,Graphics):
        super().__init__(brand,name, price, stock)
        self.Graphics = Graphics
    def shownotebook(self):
        return f"{super().showinfo()}\nGraphics : {self.Graphics}\n--------------------------------------------------------------------------------------"
    
class Cothes(Product):
    def __init__(self,brand,name, price, stock, Size):
        super().__init__(brand,name, price, stock)
        self.Size = Size
    def showclothes(self):
        return f"{super().showinfo()}\nไซส์ : {self.Size}\n--------------------------------------------------------------------------------------"
    
user1 = Mobile("samsung","Galaxy Z Fold6",53000,80,"Android")
user2 = Notebook("ASUS","ROG Strix Scar 18",144390,50,"NVIDIA GeForce RTX 4090 Graphics")
user3 = Cothes("Dior","สเวตเชิ้ตมีฮู้ดและซับใน Christian Dior Couture",110000,1000,"M,L,XL,XLL")

while True:
    print(f"ข้อมูลของ{user1.showmobile()}")
    print(f"ข้อมูลของ{user2.shownotebook()}")
    print(f"ข้อมูลของ{user3.showclothes()}")
    choiec = input('จะแก้ไขข้อมูลพิมพ์ edit หรือ exit : ')
    if choiec == 'edit':
        user1.edit("editstock")
        user1.edit("editprice")
        user2.edit("editstock")
        user2.edit("editprice")
        user3.edit("editstock")
        user3.edit("editprice")
    elif choiec == 'exit':
        print(f"ข้อมูลของ{user1.showmobile()}")
        print(f"ข้อมูลของ{user2.shownotebook()}")
        print(f"ข้อมูลของ{user3.showclothes()}")
        break
    else:
        print('ลองใหม่อีกครั้ง')