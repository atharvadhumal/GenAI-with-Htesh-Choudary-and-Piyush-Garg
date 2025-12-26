# ingredients = ["water", "milk", "black-tea"]
# ingredients.append("sugar") #appends does is adds sugar in the tuple
# print(f"Ingredients are: {ingredients}")
# ingredients.remove("water") #remove waters from the tuple
# print(f"Ingredients are: {ingredients}")

# spice_options = ["ginger", "cardamom"]
# chai_ingredients = ["water", "milk"]

# chai_ingredients.extend(spice_options)
# print(f"chai: {chai_ingredients}")
# chai_ingredients.insert(2, "black_tea")
# print(f"chai: {chai_ingredients}")


base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

#bytearray
raw_spice_data = bytearray(b"CINNAMON")
print(f"Bytes: {raw_spice_data}")