#Project to build Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
def Calc():
    """Perform any basic mathematical calculations"""
        
    e=True
    while e==True:
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        choice=int(input("Enter the Choice"))
        if choice not in [1,2,3,4]:
            print("Enter the correct choice")
        else:
            a=float(input("Enter the first number"))
            b=float(input("Enter the second number"))
            if choice==1:
                print(a+b)
            elif choice==2:
                print(a-b)
            elif choice==3:
                print(a*b)
            elif choice==4:
                print(a/b)
            
        d=input("Continue more (Y/N)?")
        if d in ['y',"Y"]:
            e= True
        else:
            e= False


        
