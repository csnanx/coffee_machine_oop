from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

user_choice = ""
while user_choice != "off":
    user_choice = input(f"What would you like? {MENU.get_items()}: ")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    if user_choice != "off" and user_choice != "report":
        ordered_item = MENU.find_drink(user_choice)
        
        if coffee_maker.is_resource_sufficient(ordered_item):
            if money_machine.make_payment(ordered_item.cost):
                coffee_maker.make_coffee(ordered_item)
