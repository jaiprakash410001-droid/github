a=int(input("enter the valure"))
b=input("enter the value to be converted either celcius to faranheit or faranheit to celsius\nEnter only 'c' or 'f")
if b=="f":
    cvf=9/5*a+32
    print("the converted value from celcius to faranheit",cvf)
elif b=="c":
    cvc=(a-32)*5/9
    print("the converted value from faranheit to celcius",cvc)
else:
    print("enter the coorect manual")