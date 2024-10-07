#Question 1
#The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of a sphere with radius 5.
#Make sure the program enters the radius from the keyboard and provides the answer in 2 decimal places.

#solution
radius = float(input("Enter the radius of the sphere:"))
volume =float((4/3)*(22/7)*radius**2)
print(f"The volume of a sphere with radius{radius} is: {volume:.2f}")

#Question 2
#create a program to calculate the area of a triangle (1/2*base*height).Base and height
# should entered using the keyboard.

#solution
base =int(input("Enter the base of a triangle:"))
height=int(input("Enter the height of a triangle:"))
area = (1/2*base*height)
print(f"The area of a triangle with base {base} and height {height} is :{area}")


# question three
#WITI has tasked you to automate a simple grading system.As apython student , write a program to
#display the grades that the students will be receiving based on the mark scored in a subject. The grade are;
#90%-100% Grade is A
#80%-89% Grade is B
#70%-79% Grade is C
#60%-69% Grade is D
#50%-59% Grade is E
#< 50% Fail

#solution
def calculate__the_grade():

    print("\n...studentgrade;")
    mark = int(input("Enter student mark :\t"))

    if mark >= 90 and mark<=100:
        print("Grade is A")

    elif  mark >= 80 and mark<=89:
        print("Grade is B")

    elif mark>= 70 and mark <=79:
        print("Grade is C")

    elif mark >= 60 and mark <=69:
        print("Grade is D")

    elif mark>=50 and mark <=59:
         print("Grade is E")

    else:
        print("fail") 
calculate__the_grade()        


#WITI Academy is proposing a Sacco to help students save their money.Design a platform that will do 
# the following .
#Welcome to WITIAcademy Sacco.
#1.Deposit Money
#2. withdraw Money
#3.check balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
#If the student selects 2, money should be withdrawn and aminimum withdrawal is 500.
#If the student selects 3, the actual balance should be displayed.

# solution.
def sacco_transactions():

    account_balance = 0
    run = 1
    while run == 1:
        print("\n Welcome to WITI Academy sacco")
        #select from :
        print("1. Deposit Money")
        print("2.Withdraw Money")
        print("3.Check Balance")

        student_choice=int(input("Enter your choice(1,2,or 3):"))
        #for transactions
        if student_choice == 1:
            print("\n... processing a deposit ....")
            deposit_amount= int(input("Enter your deposit:"))
            #if the deposit is lessthan 1000
            if deposit_amount< 1000:
                print("\ your minimum deposit is 1000")
            else:
                account_balance+= deposit_amount
                print(f"you have deposited {deposit_amount:,} and your account balance is {account_balance:,}")

        elif student_choice ==2:
            print("\n...processing a withdraw...")
            withdraw_amount =int(input("Enter the amount you would like to withdraw:"))
            if account_balance == 0:
                print("your account balance is 0")
            elif withdraw_amount < 500:
                print("\n The minimum withdraw amount is 500")
            elif withdraw_amount > account_balance:
                print(f" you have insufficient balance.")
            else:
                account_balance = account_balance - withdraw_amount
                print(f"You have withdrawn{withdraw_amount} and your account balance is {account_balance}") 

        elif student_choice ==3:
            print(f"Your account balance is {account_balance}")
        else:
            print("you have entered a wrong choice") 
            run = int(input("Enter 1 to continue and any number to exit:"))
            if run != 1:
             print("Thank you for using our sacco.")
sacco_transactions()
                             




     




  