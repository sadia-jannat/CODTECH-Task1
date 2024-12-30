print("Choose a option: ")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

option= int(input("Choose a option: "))
result=0

if(option in [1,2,3,4]):
    num1= int(input("Enter first number: "))
    num2= int(input("Enter second number: "))
    
    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
        result=num1*num2
    elif(option==4):
        result=num1//num2

else:
    print("Invalid choose")        


print("The result of operation is {}".format(result))    
                    