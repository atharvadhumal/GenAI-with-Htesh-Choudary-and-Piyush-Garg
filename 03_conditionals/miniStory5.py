order_amount = int(input("Enter the order amount: ")) #wrapped up inside 'int' so input comes as int instead of str

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is: {delivery_fees}")