import math

a = float(input("Give side a: "))
b = float(input("Give side b: "))

c = math.sqrt(a ** 2 + b ** 2)
format_c = "{:.2f}".format(c)

print(f"The length of the hypotenuse c is {format_c}")