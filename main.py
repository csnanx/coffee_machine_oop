from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

off = False
while not off:
    user_choice = input(f"What would you like? {MENU.get_items()}: ")
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        off = True
    else:
        ordered_item = MENU.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(ordered_item):
            if money_machine.make_payment(ordered_item.cost):
                coffee_maker.make_coffee(ordered_item)
