class Restaurant():
    """建立所有餐馆的父类"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurent_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurent(self):
        """打印餐馆名称"""
        print(self.restaurent_name.title() + ' ' + self.cuisine_type)

    def open_restaurant(self):
        """打印餐馆开门欢迎语"""
        print("The " + self.restaurent_name.title() + " is now opened!")

    def set_number_served(self, num_people):
        """设置已来访的人员数"""
        self.number_served = num_people

    def increament_number_served(self, num_people):
        """增加来访人员数"""
        self.number_served += num_people

    def get_number_served(self):
        """获取来访的人数"""
        return self.number_served

class IceCreamStand(Restaurant):
    """继承Restaurrent的冰淇淋店"""
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_icecream(self):
        for flavor in self.flavors:
            print(flavor)

my_icecreamstand = IceCreamStand("ice queen", "italy", ['strawbarry', 'chocolate'])
my_icecreamstand.describe_restaurent()
my_icecreamstand.open_restaurant()
my_icecreamstand.show_icecream()
my_icecreamstand.set_number_served(100)
print(my_icecreamstand.get_number_served())
my_icecreamstand.increament_number_served(50)
print(my_icecreamstand.get_number_served())

