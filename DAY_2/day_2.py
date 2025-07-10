'''
    Cho biết kiểu của các giá trị sau: -50, 1.456, False, 0.0, .5, 4+5j
    Định nghĩa hai biến num1, num2 có cùng giá trị
    Định nghĩa hai biến number1, number2 tích của chúng bằng 49
    Nhập vào tên và tuổi của bạn và in ra tên và tuổi của bạn trên cùng một hàng cách nhau bởi dấu | (xổ)
    Nhập vào một số nguyên n, số thực z, chuỗi s và in các giá trị của chúng trên các dòng riêng biệt
'''
# Kiểu của các giá trị
print("BAI 1:")
print(type(-50))      # int
print(type(1.456))    # float 
print(type(False))    # bool
print(type(0.0))      # float
print(type(.5))       # float
print(type(4+5j))     # complex
# Định nghĩa hai biến num1, num2 có cùng giá trị
print("\nBAI 2:")
num1 = num2 = 10
print(num1)
print(num2)
# Định nghĩa hai biến number1, number2 tích của chúng bằng 49
print("\nBAI 3:")
number1 = 7
number2 = 7
print(f" tích là {number1 * number2}")
# Nhập vào tên và tuổi của bạn và in ra tên và tuổi của bạn trên cùng một hàng cách nhau bởi dấu | (xổ)
print("\nBAI 4:")
name = input("Nhập tên của bạn: ")
age = input("Nhập tuổi của bạn: ")
print(f"tên của bạn là: {name} | tuổi của bạn là: {age}")
# Nhập vào một số nguyên n, số thực z, chuỗi s và in các giá trị của chúng trên các dòng riêng biệt
print("\nBAI 5:")
n = int(input("Nhập một số nguyên n: "))
z = float(input("Nhập một số thực z: "))
s = str(input("Nhập một chuỗi s: "))

print(f"Giá trị của n là: {n}")
print(f"Giá trị của z là: {z}")
print(f"Giá trị của s là: {s}")
