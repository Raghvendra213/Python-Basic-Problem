# Calculator Using if and elif

a = float(input("Enter a number A:-"))
b = float(input("Enter a number B:-"))
op = input("Enter operator (+, -, *, /): ")


if op =="+":
    print(a+b)
elif op =="-":
    print(a-b)
elif op =="*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("Not work Calculator..")