staff = [("amit", 21), ("atharva", 22), ("alan", 44)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff") #as first name only the amit was above 18 the loop stopped
        break
else:
    print(f"No one is eligible")