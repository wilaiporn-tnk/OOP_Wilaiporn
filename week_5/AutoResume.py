resume = {}
value = int(input("ต้องการป้อนทั้งหมดกี่ตัว"))
for i in range(1,value+1):
    print(f'จำนวนคนที่ {i}')
    resume['nickname'] = (str(input('กรุณากรอกชื่อเล่น : ')))
    resume['stdid'] = (int(input(f'กรุณากรอกเลขที่ : ')))
    resume['hobby'] = (str(input('กรุณากรอกงานอดิเรก : ')))
    resume['color'] = (str(input(f'กรุณากรอกสีที่ชอบ : ')))
    print(f"ข้อมูลคนที่ {str(i)}\n{resume}")