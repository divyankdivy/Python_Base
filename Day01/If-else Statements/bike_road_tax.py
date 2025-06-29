Write a program to accept the cost price of a bike and display the road tax to be paid according to the criteria:

cost_of_bike = int(input('the cost of bike is: Rs'))

tax = 0

if cost_of_bike > 100000:
    tax = (15/100)*cost_of_bike
elif cost_of_bike > 50000 and cost_of_bike <= 100000:
    tax = (10/100)*cost_of_bike
elif cost_of_bike <=50000:
    tax = (5/100)* cost_of_bike
    
print(f'tax to be paid on bike with cost Rs{cost_of_bike} is Rs{round(tax)}.')
