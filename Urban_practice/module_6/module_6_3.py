from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cord = [0,0,0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_cord = [dx, dy, dz]
        self._cord[:] = new_cord
        self._cord = [item * self.speed for item in self._cord]
        if self._cord[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cord = [item / self.speed for item in self._cord]

    def get_cords(self):
        print(f'X: {self._cord[0]}, Y: {self._cord[1]}, Z: {self._cord[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True #клюв

    def lay_eggs(self):
        numbr = randint(1,4)
        print(f'Here are(is) {numbr} eggs for you')
        pass

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = self._cord[2]
        dz = -abs(dz/2)
        self._cord[2] = dz


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = 'Click-click-click'

    def speak(self):
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()