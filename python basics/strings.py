# the first index in an array data type should be 0
# marks =[90,60,30]#example of a list in python(array)
#In arrays the first index must be 0
name ="violah"
print(name[0])
print(name[5])
#looping through strings 
for character in name:
    print(character)

address = "Kamwokya"
for item in address:
    print(item)

#SLICING IN STRINGS
# This is the accessing of a range of a character.
#example
name = "violah"
print(name[1:5])#iola
print(name[1:4])#iol
print(name[0:2])#vi 
print(name[1:2])

name = "cathy"
print(name[ :4])
message = "hello"#h(0)e(1)l(2)l(3)o(4)
print(message[ 0:3 ])#(hel)
print(message[-1])#o
print(message[-1:-4])#
print(message[-5:-3])#he
print(message[-4: ])#ello
print(message[4: ])#o
 
 #F STRINGS
name = "cathy"
age = 21
weight = 58.445
print("my name is " + name + " my age is " + str(age))
print(f"my name is {name} and am {age} years old and I weigh {weight:1f}")
total_cost = 30000
print(f"The cost of a new dress is at {total_cost:,}")
# string method
#length  len()
name = "cathy"
total_length = len(name)
print(len(name))

address ="fromkamwokya"
print(len(address))

name = "violah\n Bakuweera\n"
print(name)
name = "violah\t Bakuweera\t"
print(name)
fruit = "mango"
print(0)
print(fruit[2:5])
print(fruit[-5:-2])
name = "mbuliro\n valeria\n"
print(name)
fruit = "mango"
for item in fruit:
  print(fruit)