value = int(input("ป้อนกี่ตัว : "))
num1 =[]
for i in range (1,value+1):
    num = int(input(f"ป้อนตัวที่ {i} : "))
    num1.append(num)
    print(num1)
result = sum(num1)//len(num1)
print(f"ค่าเฉลี่ยของ {num1} คือ : {num1} = {result}")    

