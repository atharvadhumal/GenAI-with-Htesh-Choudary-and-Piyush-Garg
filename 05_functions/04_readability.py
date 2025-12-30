def calculate_bill(cups, price_per_cups):
    return cups * price_per_cups

my_bill = calculate_bill(3, 15)
print(my_bill) #one way to print the value

print("Order for table 2: ", calculate_bill(2, 50)) #another way to print the value