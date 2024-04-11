def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def exponentiation(a,b):
    return a**b

def calculator():
    """"calculator function"""
    print("Select Operation...")
    print("1.Addition")
    print("2.Subraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exponentiation")
    print("6.Quit")

    while True:
        choice = input("Enter the choice (1/2/3/4/5/6): ")

        if choice in ('1','2','3','4','5'):
            num1 = int(input("Enter the first Number:"))
            num2 = int(input("Enter the Second Number:"))
            
            if choice =='1':
              print("The Result:",add(num1,num2))
            elif choice =='2':
              print("The Result:",subtract(num1,num2))
            elif choice =='3':
              print("The Result:",multiply(num1,num2))
            elif choice =='4':
              print("The Result:",divide(num1,num2))
            elif choice =='5':
              print("The Result:",exponentiation(num1,num2))
        elif choice =='6':
              print("Exiting....")
        else:
             print("Invalid input! please try again.")
            
calculator()