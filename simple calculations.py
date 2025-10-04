a=int(input("enter the biggest number"))
b=int(input("enter the smallest number"))
while True:
    if a>b:
        addi=a+b
        mult=a*b
        subr=a-b
        divi=a/b
        qot=a//b
        rem=a%b
        print("addition",addi)
        print("subraction",subr)
        print("multiplication",mult)    
        print("division",divi)
        print("quotient",qot)
        print("reminder",rem)
else:
    print("give 'a' as the biggest  number")
   