import random
win = 0
lose = 0
draw = 0
while True :
    minigame = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(minigame)  
    choose = str(input("คุณเลือก : "))
    if choose == minigame:
        print("เสมอ")
        draw += 1
    elif choose == "ค้อน" and minigame == "กรรไกร":
        print("ชนะ")
        win += 1
    elif choose == "กรรไกร" and minigame == "กระดาษ":
        print("ชนะ")
        win += 1
    elif choose == "กระดาษ" and minigame == "ค้อน":
        print("ชนะ")
        win += 1   
    elif choose == "ออกเกม":
        break
    else:
        print("แพ้")
        lose += 1
print(f"คุณชนะทั้งหมด : {win} ครั้ง")
print(f"คุณแพ้ทั้งหมด : {lose} ครั้ง")
print(f"คุณเสมอทั้งหมด : {draw} ครั้ง")
print(f"รวมทั้งหมด : {win+lose+draw} ครั้ง")      

