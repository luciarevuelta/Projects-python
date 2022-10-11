def decision_coffee():
    coffes = ["espresso", "latte", "cappuccino"]
    while True:
        decision_user = input(
            "What would you like,(espresso/latte/cappuccino)?: ")
        if any(coffe in decision_user for coffe in coffes):
            drink = MENU[decision_user]  #almaceno dentro de la variable llamada bebida el diccionario con todos los ingredientes.
            if is_resource_sufficient(drink["ingredients"]): #si hay recursos suficientes
                payment = insert_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(decision_user, drink["ingredients"])
        elif decision_user == "off":
            break
        elif decision_user == "report":
            print(f"Water:{resources['water']} ml")
            print(f"Milk: {resources['milk']} ml")
            print(f"Coffee:{resources['coffee']} g")
            print(f"money: ${profit}")  
decision_coffee()


def is_resource_sufficient(order_ingredients):
    """Devuelve True cuando se puede realizar el café (orden) y False cuando no.
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNIE = 0.01
def insert_coins():
        print("Please insert coins")
        while True:
            try:
                quarters = int(input("How many quartes?"))
                dimes = int(input("How many dimes?"))
                nickles = int(input("How many nickles?"))
                pennies = int(input("How many pennies"))
            except ValueError:
                    print("That's not a float value! Repeat again!")
            else:
                monetary_value = int(round(QUARTER * quarters + DIME * dimes + NICKLE * nickles + PENNIE * pennies,2))
                return monetary_value
            #if (quarters.isnumeric() and dimes.isnumeric() and nickles.isnumeric() and pennies.isnumeric()):
                #monetary_value = round(QUARTER * quarters + DIME * dimes + NICKLE * nickles + PENNIE * pennies,2)
                #return monetary_value
insert_coins()

def is_transaction_successful(money_received, drink_cost):
    """Devuelve True cuando el pago es aceptado oo False si el dinero es insuficiente"""
    if  money_received > drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.")
        return False
    
   def make_coffee(drink_name,order_ingredients):
    "Required ingredients"
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")
