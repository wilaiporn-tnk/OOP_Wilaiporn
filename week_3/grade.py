score = int(input("กรุณาใส่คะแนน"))
if score > 100:
    print("Error")
elif score >= 80 :
    print("4")
elif score >= 70 :
    print("3")
elif score >= 60 :
    print("2")
elif score >= 50 :
    print("1")
elif score < 0 :
    print("Error")
else:
    print("0")
    print("สอบตก")
    print("อยากสอบแก้ไหม")
solve = str(input("พิมพ์ Y or N\n"))
if solve == "Y":
    print("คะแนนที่ขาด " + str(50-score)+ "คะแนน")
elif solve == "N":
    print("คุณยังไม่ผ่าน")
else :
    print("ป้อนค่าที่ถูกต้อง")

