a=int(input("enter the value"))
b=input("would you like to change your value into miles or km or m\n please enter only 'miles' or 'km' or 'm'")
if b=="km":
    cvk =  a*1.609
    print("converted miles to kilometer",cvm)
elif b=="miles":
    cvm =  a*0.621
    print("coverted kilometer to miles",cvk)
elif b=="m":
    cvme = a*1000
    print("converted km to meter",cvme)
else:
    print("give only numbers")