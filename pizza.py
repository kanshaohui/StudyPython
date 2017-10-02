def make_pizza(size, *toppings):
    """打印顾客点的所有配件"""
    print(toppings)
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-  " + topping)

make_pizza(16,'pepperoni')
make_pizza(12, 'mushrooms', 'greeen peppers', 'extra cheese')