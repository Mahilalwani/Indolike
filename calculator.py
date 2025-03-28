print("************************************************")
print("This is your Simple Calculator")
print("************************************************")

def Calculator(a,b):
    sum=a+b
    diff=a-b
    mul=a*b
    if b!=0:
        div=a/b
    else:
        print("Division cannot be done by 0")
    exp=a**b
    per=(a/100)*b
    mod=a%b
    print(f"For your given numbers, these are the calculations:\n Sum:{sum}\n Difference:{diff}\n Product:{mul}\n Division:{div}\n Power:{exp}\n Percentage:{per} \n Modulus:{mod}")    

print("Please enter the operands\n")
a=int(input("Enter the first number\n"))
b=int(input("Enter the second number\n"))  
Calculator(a,b)  