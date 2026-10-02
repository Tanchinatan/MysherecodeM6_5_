# พัฒนาจากต้นแบบ โดย: โปรแกรมคำนวณพื้นที่รูปสามเหลี่ยม
import math

def read_positive(prompt):
    """รับค่าตัวเลขที่มากกว่า 0 ถ้าไม่ถูกต้องจะคืน None"""
    try:
        value = float(input(prompt))
    except ValueError:
        print("ข้อผิดพลาด: กรุณากรอกเป็นตัวเลข")
        return None
    if value <= 0:
        print("ข้อผิดพลาด: ค่าต้องมากกว่า 0")
        return None
    return value

print("=== โปรแกรมคำนวณพื้นที่รูปทรงเรขาคณิต ===")
print("1. สี่เหลี่ยมมุมฉาก")
print("2. สามเหลี่ยม")
print("3. วงกลม")

choice = input("เลือกรูปทรงที่ต้องการคำนวณ (1-3): ").strip()

if choice == "1":
    width = read_positive("กรอกความกว้าง: ")
    length = read_positive("กรอกความยาว: ") if width else None
    if width and length:
        print(f"พื้นที่สี่เหลี่ยมมุมฉากคือ: {width * length:.2f} ตารางหน่วย")

elif choice == "2":
    base = read_positive("กรอกความยาวฐาน: ")
    height = read_positive("กรอกความสูง: ") if base else None
    if base and height:
        print(f"พื้นที่สามเหลี่ยมคือ: {0.5 * base * height:.2f} ตารางหน่วย")

elif choice == "3":
    radius = read_positive("กรอกรัศมีวงกลม: ")
    if radius:
        print(f"พื้นที่วงกลมคือ: {math.pi * radius ** 2:.2f} ตารางหน่วย")

else:
    print("เลือกเมนูไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")
