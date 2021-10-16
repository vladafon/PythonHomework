#from LibaDZ import functions as f

#@f.type_check(a=int,pow=int)
#@f.cache_decorator
#def power(a, pow=2):
    #return a**pow

#print(power(3, 9))
#print(power(2, 4))
#print(power(2, 5))
#print(power(2, 4))
#print(power(3, 9))
#print(power(3,2))
#print(power(3,))

#print(power(3,'3'))

#print(power('3',4))



class Human(object):

    default_name = ''
    default_age = 0

    def __init__(self, name, age):
        self.default_name = name
        self.default_age = age
        self._money = 0
        self._house = None


    def info(self):
        print(self.default_name)
        print(self.default_age)
        print(self._money)
        print(self._house)

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def __make_deal(self, price, house, discount):
        self._money -= house.final_price(discount)
        self._house = house

    def earn_money(self):
        self._money += 80000


    def buy_house(self, house, discount):
        if (house.final_price(discount) > self._money):
            print('Иди на шахты работай, потом придешь!')
        else:
            self.__make_deal(house._price, house, discount)




class House(object):

    _area = 0 #м2
    _price = 0


    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - (discount*self._price/100)


class SmallHouse(House):
    def __init__(self, price):
        House.__init__(self, 40, price)


##########################################

Human.default_info()

bednyi_student = Human('Vasya Pupkin', 22)

bednyi_student.info()

obshaga = SmallHouse(3000)

bednyi_student.buy_house(obshaga, 20)

bednyi_student.earn_money()

bednyi_student.buy_house(obshaga, 20)

bednyi_student.info()

