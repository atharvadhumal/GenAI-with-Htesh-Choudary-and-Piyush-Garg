def update_order():
    chai_type = "elaichi"
    def kitchen():
        nonlocal chai_type #something which is outisde the local scope of function can be accessed by using nonlocal
        chai_type = "kesar"
    kitchen()
    print(f"After kitchen update", chai_type)
    
update_order()