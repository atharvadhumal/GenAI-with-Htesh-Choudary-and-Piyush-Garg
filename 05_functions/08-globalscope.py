chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type #global keywords with this we can access any global scopes
        chai_type = "irani"
    kitchen()
    
front_desk()
print("final global chai:", chai_type)