try:
    price = int(input("ราคา"))
    if price >= 5000:
        print(f"ได้รับส่วนลด 20 % = {price-price*0.2}")
    elif price >= 2000 and price <4999:
        print(f"ได้รับส่วนลด 10 % = {price-price*0.1}")
    elif price == 0:
        raise ZeroDivisionError
    elif price < 0:
        raise Exception
    else:
        print("ไม่ได้รับส่วนลด")
except ValueError:
    print("ใส่เฉพาะตัวเลข")
except ZeroDivisionError:
    print("ห้ามใส่ 0")
except:
    print("ห้ามใส่ค่าติดลบ")
