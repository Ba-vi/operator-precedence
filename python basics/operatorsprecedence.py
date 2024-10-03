#operator precedence
#descibes the order in which operations are performed in anexpression.
#operators with ahigher precedence are always executed first.
#examples
result= 3*4+5
print(f"The result of the numbers is :{result}")
result_two = 3*(4+5)
print(result_two)
result_three = 3*4+5-1
print(result_three)
result_four = 3*(4+5)-1
print(result_four)

#General operator precedence
# What will be the out put of the following expression.
result_five = 5*3**2
print(result_five)

result_six = (5+3)*2**2-10/2
print(result_six)

result_seven =25/5 + 2*1
print(result_seven)#when we have a division operator the return type is a float.

result_eight = (25/5) + 2*1
print(result_eight)