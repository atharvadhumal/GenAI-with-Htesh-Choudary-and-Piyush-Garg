essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices # | is the union spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices # & is intersection symbol
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices 
print(f"only in essential: {only_in_essential}")

print(f"Is 'cloves' in essential spices? {'cloves' in optional_spices}") #membership test

#frozen Set
