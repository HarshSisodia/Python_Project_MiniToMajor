#Using the function and if-else condition to perform basic calculator operations.
def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def multiplication(num1,num2):
    return num1*num2

def division(num1,num2):
     if(num2==0):
         return("Cannot divide by zero.")
     else:
         return num1/num2
     
def avg(num1,num2):
    return (num1+num2)/2

def modular(num1,num2):
     if num2 == 0:
        return "Cannot perform modulus with zero!"
     return num1%num2
     
#User Input
while True:

    print("\n========== BASIC CALCULATOR ==========")

    print("1. Addition")

    print("2. Subtraction")

    print("3. Multiplication")

    print("4. Division")

    print("5. Average")

    print("6. Modulus")

    print("7. Exit")

    print("======================================")



    select=int(input("Select the operation Number (1-7): "))
    if select==7:
        print("Thankyou for using the calculator")
        break
    elif select not in [1, 2, 3, 4, 5, 6]:
        print("Invalid User Input! Please try again.")
        continue

    num1=float(input("Enter the First Number: "))
    num2=float(input("Enter the Second Number: "))


    #Operations:
  

    if select==1:
        print(num1,"+",num2,"=",\
          addition(num1,num2))
    
    elif select==2:
        print(num1,"-",num2,"=",\
          subtraction(num1,num2))

    elif select==3:
        print(num1,"*",num2,"=",\
          multiplication(num1,num2))
      
    elif select==4:
        print(num1,"/",num2,"=",\
         division(num1,num2))
    

    elif select==5:
        print("(" ,num1, "+" ,num2, ")", "/", "2", "=",\
         avg(num1,num2))
    

    elif select==6:
        print(num1,"%",num2,"=",\
         modular(num1,num2))

  #Close the calculator
    
    choice=input("Do You want to continue using the calculator(Y/N): ")

    if choice.lower()=="y":
        continue
    elif choice.lower()=="n":
        print("Thank you for using the calculator!")
        break
    else:
         print("Invalid choice! Please enter Y or N.")

