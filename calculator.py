

def add(a, b):
    result = a +b
    print("a+b =", result)

def sub(a, b):
    result = a-b
    print("a-b =", result)

def multi(a, b):
    result = a*b
    print("a*b=", result)

def div(a,b):
    result = a/b
    print("a/b=", result)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operater: ")

if op=="+":
    add(a,b)
elif op == "-":
    sub(a,b)
elif op=="*":
    multi(a,b)
elif op=="/":
    div(a,b)
else:
    print("Invaild Number")
