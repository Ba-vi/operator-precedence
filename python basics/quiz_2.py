# write a program that takes two numbers as inputs and displays their sum,product, difference and quotient.

first_number=  int(input("Enter first number: "))
second_number= int(input("Enter second number: "))
sum = first_number  +   second_number
print(f"The sum of {first_number} and {second_number} is :  {sum}")
product = first_number *  second_number
print( f"The product of {first_number} and {second_number} is :{product}")
difference = second_number - first_number
print(f"The difference of {first_number} and {second_number} is: {difference}" )
quotient = second_number / first_number
print(f"The quotient of the {first_number} and {second_number} is: {quotient}")
modulus = second_number  %  first_number
print(f"The modulus of the {first_number} and {second_number} is : {modulus}")
floor_division = second_number // first_number
print(f"The floor division of the {first_number} and {second_number} is : {floor_division}")


#write a program that compare two integers and prints whether the first number is greater than , less than or equal to the second number.
# answer(2)(comparison operators)(if loop)
first_number = int(input("Enter the first_number:"))
second_number = int(input("Enter the second_number:"))
if first_number > second_number :
    print(f" {first_number} is greater than {second_number}")
elif first_number < second_number :
    print(f" {first_number} is less than {second_number}")
else :
    print(f"They are equal")


# write  a program that checks if a given number is between 10 and 20 using logical operators(20 is inclusive)
number = int(input("Enter the number:"))
print(number > 10 and number <= 20)
print(number > 10 or  number <=20 )
print(not(number >10 and number <=20))

# write the program that prints the squares if all integers from  1-10 using a for loop.
integers = [1,2,3,4,5,6,7,8,9,10]
for y in integers:
 print(y**2)


# write a program that asks a user for their age ,if the age is greater or equal to 18, print adult and you are  qualified else you tell them you are not qualified.
age=int(input("Enter your age:"))
if age >18 :
  print(f" {age} ,adult and you are qualified.")
elif age == 18 :
    print(f" {age} ,adult and  you are qualified.")
else :
  print(f"{age},you are not qualified")


#we have the following students details and marks enter these details from the keyboard 
#student name=Ritah liz
#student number=SEP23/BCS/14
#programing=78
#data science=89
#computer applications=55
#calculate the average mark and print the answer in  3 decimal places.
student_name = (input("Enter the student name : "))
student_number = (input("Enter the student number: "))
programming =int(input("Enter  the programming mark: "))
data_science =int(input("Enter  the data science mark: "))
computer_science = int(input("Enter the computer science mark: "))
total_mark =(programming + data_science + computer_science)
course_units = 3
average_mark = total_mark  /  course_units
print(f" The average mark of{student_name} with{student_number} is:{average_mark:.3f}")


# question2: 
# write aprogram that converts c temp to F.the program should ask  the user to enter the temp in C degrees
#and then display the temp converted to F
temp_in_celcius = float(input("Enter temperature in celcius degrees : "))
fahrenheit_degrees = float(temp_in_celcius *1.8) + 32
print(f"The temperature in degrees fahrenheit is: { fahrenheit_degrees : .1f}")


# A car's miles per gallon can be calculated with following formular as written.
#mpg=milesdriven/gallons of gas used
#write a program that asks a user for number of miles driven and gallons used and display the results
miles_driven = int(input("Enter miles driven:"))
gallons_of_gas_used =int(input("Enter gallons of gas used:"))
mpg = miles_driven/gallons_of_gas_used
print(f" The number of miles driven and gallons used is :{mpg :.2f}")



