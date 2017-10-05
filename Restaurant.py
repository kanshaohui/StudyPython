class Restaurant():
    """建立所有餐馆的父类"""
    def __init__(self, restaurant_name, cuision_type):
        self.restaurent_name = restaurant_name
        self.cuision_type = cuision_type
        self.number_served = 0

    def describe_restaurent(self):
        """打印餐馆名称"""
        print(self.restaurent_name + ' ' + self.cuision_type)

    def open_restaurant(self):
        """打印餐馆开门欢迎语"""
        print("The " + self.restaurent_name + " is now opened!")

    def set_number_served(self, num_people):
        """设置已来访的人员数"""
        self.number_served = num_people

    def increament_number_served(self, num_people):
        """增加来访人员数"""
        self.number_served += num_people

class IceCreamStand(Restaurant):
    """继承Restaurrent的冰淇淋店"""
    def __init__(self, restaurant_name, cuision_type, flavors):
        super().__init__(restaurant_name, cuision_type)
        self.flavors = flavors

    def show_icecream(self):
        for flavor in self.flavors:
            print(flavor)

my_icecreamstand = IceCreamStand("ice queen", "italy", ['strawbarry', 'chocolate'])
print(my_icecreamstand.describe_restaurent())
print(my_icecreamstand.open_restaurant())