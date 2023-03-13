class Pizza:

    def __init__(self):
        # self.toppings = toppings
        self.cost = 0
        # self.description = "Pizza"

    def get_description(self):
        return self.get_description()

    def get_cost(self):
        return self.cost


class MargheritaPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.cost = 18

    def get_description(self):
        return "A Margherita Pizza"

    def get_cost(self):
        return self.cost


class TurkishPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.cost = 15

    def get_description(self):
        return "A Turkish Pizza"

    def get_cost(self):
        return self.cost


class ClassicPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.cost = 10

    def get_description(self):
        return "A Classic Pizza"

    def get_cost(self):
        return self.cost


class DominosPizza(Pizza):

    def __init__(self):
        super().__init__()
        self.cost = 20

    def get_description(self):
        return "A Dominos Pizza"

    def get_cost(self):
        return self.cost


class Decorator(Pizza):

    def __init__(self, number):
        super().__init__()
        self.number = number
        self.cost = 0

    def get_description(self):
        if self.number == 11:
            olive = Olive()
            olive.get_description()
            return olive.get_description()

        elif self.number == 12:
            mushroom = Mushroom()
            mushroom.get_description()
            return mushroom.get_description()

        elif self.number == 13:
            cheese = Cheese()
            cheese.get_description()
            return cheese.get_description()

        elif self.number == 14:
            beef = Beef()
            beef.get_description()
            return beef.get_description()

        elif self.number == 15:
            onion = Onion()
            onion.get_description()
            return onion.get_description()

        elif self.number == 16:
            corn = Corn()
            corn.get_description()
            return corn.get_description()

    def get_cost(self):
        if self.number == 11:
            olive = Olive()
            olive.get_cost()
            return olive.get_cost()

        elif self.number == 12:
            mushroom = Mushroom()
            mushroom.get_cost()
            return mushroom.get_cost()

        elif self.number == 13:
            cheese = Cheese()
            cheese.get_cost()
            return cheese.get_cost()

        elif self.number == 14:
            beef = Beef()
            beef.get_cost()
            return beef.get_cost()

        elif self.number == 15:
            onion = Onion()
            onion.get_cost()
            return onion.get_cost()

        elif self.number == 16:
            corn = Corn()
            corn.get_cost()
            return corn.get_cost()
        else:
            return 0


class Olive:
    def __init__(self):
        super().__init__()
        self.number = 11
        self.cost = 1

    def get_cost(self):
        return 1

    def get_description(self):
        return "olive"


class Mushroom:
    def __init__(self):
        super().__init__()
        self.cost = 2

    def get_cost(self):
        return 2

    def get_description(self):
        return "mushroom"


class Cheese:
    def __init__(self):
        super().__init__()
        self.cost = 3.50

    def get_cost(self):
        return 3.50

    def get_description(self):
        return "cheese"


class Beef:
    def __init__(self):
        super().__init__()
        self.cost = 6.50

    def get_cost(self):
        return 6.50

    def get_description(self):
        return "beef"


class Onion:
    def __init__(self):
        super().__init__()
        self.cost = 2.50

    def get_cost(self):
        return 2.50

    def get_description(self):
        return "onion"


class Corn:
    def __init__(self):
        super().__init__()
        self.cost = 1.20

    def get_cost(self):
        return 1.20

    def get_description(self):
        return "corn"
