num = int(input("ใส่ค่า"))
loop = 1
while loop <= 24:
    if num * loop / 2 % 2 != 0:
        print(f"{num} X {loop} = {num*loop}")
    loop += 1