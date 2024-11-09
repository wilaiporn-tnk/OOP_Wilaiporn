#โปรแกรมสูตรคูณแบบรับค่า คูณจาก 1 ไป 24 แสดงผลเฉพาะผลลัพธ์ที่หารด้วย 2 แล้วเป็นเลขคี่
num = int(input("ใส่ค่า"))
for loop in range(1,24+1,1) :
    sum = num * loop
    if sum / 2 % 2 != 0:
        print(f"{num} x {loop} = {sum}")