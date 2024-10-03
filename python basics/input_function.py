#INPUT FUNCTION
#input()
student_name = input("enter your name : ")
student_age = input("enter your age:")
print(" my name is " + student_name + " and my age is " + student_age)
print(type(student_age),type(student_name))
student_address= input("enter your address:")
student_best_dish =input("enter your best dish:")
student_best_movie =input("enter your best movie:")
print(" I live at " + student_address + " my best dish " + student_best_dish + " my best movie is" +student_best_movie)


# f string
name ="violah"
age = 25
address="bulenga"
print( "my name is " + name + " iam " + str(age) + " i live at " + address)
print(f"my name is " + {name} + " iam " + {age} + "i live at " + {address})
