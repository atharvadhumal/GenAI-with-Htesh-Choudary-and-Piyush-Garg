masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ration = 2, 1
print(f"Ratio is Ginger{ginger_ratio} and Cardamom{cardamom_ration}")
ginger_ratio, cardamom_ration = cardamom_ration, ginger_ratio
print(f"Ratio is Ginger{ginger_ratio} and Cardamom{cardamom_ration}")

#membership
print(f"Is cloves in masala_spices? {'cloves' in masala_spices}")