def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2==0:
        print("Division by Zero is not allowed.")
    else:
        return num1/num2
calc_over=False
while not calc_over:
    result=0
    num1=int(input("Enter the first number---"))
    operation=input("Enter the operation(+,-,*,/):")
    num2=int(input("Enter the next number---"))
    if operation=="+":
        result=add(num1,num2)
    elif operation=="-":
        result=sub(num1,num2)
    elif operation=="*":
        result=mul(num1,num2)
    elif operation=="/":
        result=div(num1,num2)
    else:
        print("Invalid operation")
    
    print(f"result={result}")
    print("-"*20)

    choice=input("Do you want to calculate again'y,n':").lower()
    if choice=="y":
        calc_over=False
    elif choice=="n":
        calc_over=True
        print("Goodbye")
    