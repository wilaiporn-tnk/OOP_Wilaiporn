print("โปรดกรอกชื่อ")
name = str(input("ใส่ชื่อ"))
print("โปรดกรอกอายุ")
age = int(input("ใส่อายุ"))
print("โปรดกรอกรหัสประจำตัว")
stdID= int(input("ใส่รหัสประจำตัว"))
print("โปรดกรอกระดับชั้น")
Level = int(input("ใส่ระดับชั้น"))
print("โปรดกรอกชื่อเล่น")
nicname = str(input("ใส่ชื่อเล่น"))
print("โปรดกรอกส่วนสูง")
height= float(input("ใส่ส่วนสูง"))
print("โปรดกรอกน้ำหนัก")
weight= float(input("ใส่น้ำหนัก"))
print(f"ชื่อ : {name},อายุ : {age}ปี")
print(f"รหัสประจำตัว : {stdID},ระดับชั้น : {Level}")
print(f"ชื่อเล่น : {nicname}")
print(f"ส่วนสูง {height}เซนติเมตร, น้ำหนัก : {weight}กิโลกรัม")
num = height + weight
print("ส่วนสูง + น้ำหนัก =",(num))