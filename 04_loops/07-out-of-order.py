flavours = ["Ginger", "out of stock", "lemon", "discontinued", "tulsi"]

for flavour in flavours:
    if flavour == "out of stock": #when found this it continued
        continue
    if flavour == "discontinued": #when found this it stopped
        break
    print(f"{flavour} item found")