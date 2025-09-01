#在列表中移动位置
'''unconfirmed_users = ['alice','brain','cline']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user : {current_user.title()}")
    confirmed_users.append(current_user)
print("The following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())'''
#函数的基础使用
'''def city_country(city,country):
    name=f"{city} {country}"
    return  name
while True:
    print("enter 'q' to quit")
    cit = input("city name: ")
    if cit == 'q':
        break
    countr = input("country name: ")
    if countr == 'q':
        break
    city_countryname=city_country(cit,countr)
    print(f"The name is {city_countryname}")'''
#函数练习
'''from sand import sandwishes

# 从键盘录入 toppings
toppings_list = []
while True:
    topping = input("请输入你想要的三明治的 topping（输入 'q' 结束）：")
    if topping == 'q':
        break
    toppings_list.append(topping)

# 调用函数
sandwishes(*toppings_list)'''
#类的基础练习
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,):
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served=0
    # @classmethod 这是将其变成类方法（可选方法之一）
    def describe_restaurant(self):
        print(f"the restaurant named {self.name} serves {self.type} cuisine!")
        print("the restaurant is the top1")
    def open_restaurant(self):
        print(f"the restaurant {self.name} is open")
        print(f"the restaurant has served {self.number_served} people")
    #使用函数来更新就餐人数
    '''def update_num_served(self,number_new):
        self.number_served=number_new'''

'''my_restaurant=Restaurant('gongfu','Chinese food')

my_restaurant.describe_restaurant()
my_restaurant.update_num_served(236)#修改就餐人数：从0到236
my_restaurant.open_restaurant()'''
#继承的练习如下：
class IceCreamStand(Restaurant):
    #初始化IceCreamStand，继承Restaurant类
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=[]#这里创建了一个空列表
    #添加口味
    def add_flavors(self,flavors):
        self.flavors.append(flavors)
    #展示口味
    def display_flavors(self):
        print("我们有以下冰淇淋：")
        for flavor in self.flavors:
            print(f"-{flavor}")
#现在来调用
ice_cream_stand=IceCreamStand('dairy queen','icecream')
ice_cream_stand.add_flavors('芋泥')
ice_cream_stand.add_flavors('香草')
ice_cream_stand.add_flavors('巧克力')
ice_cream_stand.add_flavors('杨枝甘露')
ice_cream_stand.display_flavors()






