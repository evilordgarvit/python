import time

name = input("emter your name:")
print(f"hello,{name}")
time.sleep(1.5)
print("i am a calculater created by evilord")
time.sleep(1.5)
print("Code : + = 1, - = 2, x = 3, / = 4")
count = 0

while count < 5:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter operation code (1, 2, 3, or 4): "))
    
    if c == 1:
        print(f"{a} + {b} = {a + b}")
    elif c == 2:
        print(f"{a} - {b} = {a - b}")
    elif c == 3:
        print(f"{a} x {b} = {a * b}")
    elif c == 4:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Sorry! But the code you entered is not valid.")
    time.sleep(1)
    while True:
        start=input("the task is compleated do you won't to do more??")

        if start.lower() == "yes":
            print("let me start it again")
            break
        elif start.lower() == "no":
            print("bye bye!! have a nice day")
            exit()
        else:
            print("invalid input. please enter'yes' or 'no'.")
            time.sleep(2)
            continue
        
    time.sleep(2)
count += 1
