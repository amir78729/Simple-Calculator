from math import *

continue_or_not = True
while True:
    if continue_or_not:
        a = float(input("type A : "))
    op = input("type op : ")
    if op == "=" or op == "clear":
        continue_or_not = True
        continue
    elif op == "cos":
        print("cos(" + str(a) + ") =")
        a = a % 360
        a = radians(a)
        a = cos(a)
        print(a)
        continue_or_not = False
        continue
    elif op == "sin":
        print("sin(" + str(a) + ") =")
        a = a % 360
        a = radians(a)
        a = sin(a)
        print(a)
        continue_or_not = False
        continue
    elif op == "!":
        print("(" + str(a) + ")! =")
        a = factorial(a)
        print(a)
        continue_or_not = False
        continue
    elif op == "sqrt":
        print("√(" + str(a) + ") =")
        a = sqrt(a)
        print(a)
        continue_or_not = False
        continue
    elif op == "inverse":
        print("1 / (" + str(a) + ") =")
        if a == 0:
            print("∞")
            continue_or_not = True
            continue
        else:
            a = 1/a
            print(a)
            continue_or_not = False
            continue
    elif op == "minus":
        print("-(" + str(a) + ") =")
        a *= -1
        print(a)
        continue_or_not = False
        continue
    elif op == "tg" or op == "tan":
        print("tan(" + str(a) + ") =")
        a = a % 360
        if a % 180 == 0:
            a = 0
        elif a % 90 == 0:
            if a < 180:
                print("∞")
            else:
                print("-∞")
            continue_or_not = True
            continue
        elif a % 360 == 45 or a % 360 == 225:
            a = 1.0
        elif a % 360 == 135 or a % 360 == 315:
            a = -1.0
        else:
            a = radians(a)
            a = tan(a)
        print(a)
        continue_or_not = False
        continue
    elif op == "exp":
        print("exp(" + str(a) + ") =")
        a = exp(a)
        print(a)
        continue_or_not = False
        continue
    b = float(input("type B : "))

    if op == "+":
        print(str(a) + " + " + str(b) + " =")
        a = float(a) + float(b)
        continue_or_not = False

    elif op == "-":
        print(str(a) + " - " + str(b) + " =")
        a = float(a) - float(b)
        continue_or_not = False

    elif op == "*":
        print(str(a) + " * " + str(b) + " =")
        a = float(a) * float(b)
        continue_or_not = False

    elif op == "/":
        print(str(a) + " ÷ " + str(b) + " =")
        if b == 0:
            print("∞")
            continue_or_not = True
            continue
        else:
            a = float(a) / float(b)
            continue_or_not = False

    elif op == "^":
        print(str(a) + " ^( " + str(b) + " ) =")
        a = float(a)**float(b)
        continue_or_not = False

    print(a)
    print("------------------")


