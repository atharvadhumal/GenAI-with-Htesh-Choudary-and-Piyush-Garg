chai_order = dict(type="masala chai", size="Large", sugar=2)
print(f"chai order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")
del chai_recipe["liquid"] #deletes the milk
print(f"Recipe: {chai_recipe}")


#membership testing: done to check it something exist in the data
print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger chai", "size": "Medium", "sugar":1}
# print(f"Order details (keys): {chai_order.keys()}") #keys here are types, size, sugar to which we have defined a value
# print(f"Order details (values): {chai_order.values()}") #values are something we have assigned to a key, here are Ginger chai, Medium, 1
# print(f"Order details (items): {chai_order.items()}") #items means full things like 'type', 'Ginger chai'), ('size', 'Medium'), ('sugar', 1)

last_item = chai_order.popitem()
print(f"removed last item: {last_item}")