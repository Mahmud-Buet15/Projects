from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# TODO 1: print report
# TODO 2: check if  resources are sufficient?
# TODO 3: process coins
# TODO 4: check if transactions  are sufficient?
# TODO 5: make coffee




m=Menu()

c_maker=CoffeeMaker()

m_machine=MoneyMachine()

is_on=True

# while is_on:
#     inp=input(f"What would you like?({m.get_items()}):")
    
#     if inp="off":
#         is_on=False
    
#     elif inp=="report":
#         c_maker.report()
#         m_machine.report()
        
#     elif inp=="espresso":
#         if c_maker.is_resource_sufficient(espresso):
#             if m_machine.make_payment(1.5):
#                 c_maker.make_coffee(espresso)
    
#     elif inp=="latte":
#         if c_maker.is_resource_sufficient(latte):
#             if m_machine.make_payment(2.5):
#                 c_maker.make_coffee(latte)
    
#     elif inp=="cappuccino":
#         if c_maker.is_resource_sufficient(cappuccino):
#             if m_machine.make_payment(3):
#                 c_maker.make_coffee(cappuccino)
            
    

while is_on:
    
    options=m.get_items()
    inp=input(f"What would you like?({options}):")
    
    if inp=="off":
        is_on=False
    
    elif inp=="report":
        c_maker.report()
        m_machine.report()
    
    else:
        drink=m.find_drink(inp)    #this is a instance of MenuItem
        if c_maker.is_resource_sufficient(drink):
            if m_machine.make_payment(drink.cost):
        
                c_maker.make_coffee(drink)
                
            
        
        
    
    