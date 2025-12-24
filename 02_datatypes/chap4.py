is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling #upcasting here the 5 and the true got added and 6 number came
print(f"Total actions: {total_actions}")

milk_present = 1 # no milk
print(f"Is there milk? {bool(milk_present)}") #automatically converts 0 and 1 to true/flase