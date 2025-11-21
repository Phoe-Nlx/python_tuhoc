"""
- kiểu dữ liệu
- biến là tên của giá trị
- hàm input() 
- hàm print()

"""
# type() : kiểm tra kiểu dữ liệu
# values = [-50, 1.456, False, 0.0, .5, 4+5j]

# ===========================================
# print(type(2))
# print(type(True))
# print(type(""))

# _1 = 4
# _2 = 4.4
# _3 = 4+5j
# print(type(_1))
# print(type(_2))
# print(type(_3))

# ===========================================
print(type(-50))
print(type(1.456))
print(type(False))
print(type(0.0))
print(type(.5))
print(type(4 + 5j))

print("BAI 2")

num1 = num2 = 2
print(num1)
print(num2)


print("BAI 3")

name = input("Nhap ten cua ban: ")
age = input("Nhap tuoi cua ban: ")
print("Ten cua ban la:",name,"| tuoi cua ban la: ", age)

print("BAI 5")

int_n = int(input("Nhap mot so nguyen: "))
float_z = float(input("Nhap mot so thuc: "))
str_s = str(input("Nhap mot chuoi: "))
print("So nguyen vua nhap la: ", int_n)
print("So thuc vua nhap la: ", float_z)
