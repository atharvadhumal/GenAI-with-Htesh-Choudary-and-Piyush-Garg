# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisble, remainder is {remainder}")

# value = 13

# if (remainder:= value % 5):
#     print(f"Not divisble, remainder is {remainder}")
    

# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"not available - {requested_size}")

flavours = ["masala", "ginger", "mint", "lemon"]

print(f"Available flavours: {flavours}")

while (flavour := input("choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} not available")
    
print(f"you choose {flavour} chai")