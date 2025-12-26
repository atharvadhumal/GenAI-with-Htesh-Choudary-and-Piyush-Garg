chai_type = "Ginger chai"
customer_name = "priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8]}") #the 2 here means every second character will get print

label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")
print(f"Non-encoded : {label_text}")
print(f"Encoded : {encoded_label}")
