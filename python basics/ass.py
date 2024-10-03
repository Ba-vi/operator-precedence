#ASSIGNMENT OPERATORS
sum = 5
sum +=6
print(sum)
# Given that we have two products a laptop and a mouse, suchthat the price of a laptop is 300,000
#and the price of a mouse is 50,000.use a for loop to find the total sum of the products.
laptop = 300000
mouse = 50000
sum = 0
product_prices = [laptop , mouse]
for price in product_prices:
      sum+=price
print(f"The total sum of the product is : {sum:,}")# the print shouldnot be indented when we  need 
#the final sum(one sum)
    


