Sum = 0
while True:
    try:
        price = str(input("ใส่ราคาสินค้า (พิมพ์ exit เพื่อออก) : "))
        if price == "exit":
            print(f"ยอดรวมปัจจุบัน : {sum}")
            break
        price = int(price)
        if price == 0:
            raise ZeroDivisionError
        elif price < 0:
            raise Exception
        else:
            sum += price
            print(sum)
    except ValueError:
        print("กรุณาใส่ตัวเลขเท่านั้น")
    except ZeroDivisionError:
        print("ราคาสินค้าต้องมากกว่า 0")
    except:
        print("ราคาสินค้าต้องไม่ติดลบ")


