def serve_chai():
    chai_type = "masala" #local scope
    print(f"inside function {chai_type}")
    
chai_type = "Lemon"
serve_chai()
print(f"Outside function {chai_type}")

def chai_counter():
    chai_order = "lemon" #enclosing scope
    def print_order():
        chai_order = "Ginger"
        print(f"Inner: ", chai_order)
    print_order()
    print(f"outer: ", chai_order)

chai_order = "tulsi" #global scope
chai_counter()
print(f"Global: ", chai_order)