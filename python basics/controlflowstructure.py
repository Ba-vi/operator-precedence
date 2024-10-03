#control flow structures.
#determine the structure in which the program can be executed basing on the loops or conditions.
#conditional statements
#These are statements that execute a program basing on a particular condition.e.g if, elif,else.
#We execute if statement if the condition is true.we execute elif if the if condition is false.
#example
#create a program that asks a user for the food type bought from the market.The program should print you
#bought chicken if the user bought chicken or print liver if the user bought liver else the program should print
#fish.

food_type = input("Enter the food type bought:").lower()

if food_type =="chicken":
    print(f"You bought chicken from the market.")

elif food_type =="liver":
    print(f"you bought liver from the market.")
elif food_type =="fish":
    print(f"you bought fish from the market.")

else:
    print(f"Please choose from chicken , fish or liver.")# approach one

#approach two
food_type = input("Enter the food type bought:").lower()
if food_type != "liver" or food_type != "chicken" or food_type != "fish":
    print("please select from fish, liver or chicken.")

if food_type =="chicken":
    print(f"You bought chicken from the market.")

elif food_type =="liver":
    print(f"you bought liver from the market.")
elif food_type =="fish":
    print(f"you bought fish from the market.")

else:
    print(f"You have bought fishfrom the market.") 
