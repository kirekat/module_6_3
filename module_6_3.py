import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        self._cords[2] = dz * self.speed
        if dz in self._cords < 0:
            print("It's too deep, i can't dive : " )


    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful: ")
        else:
            print("Be careful, i'm attacking you 0_0" )

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        eggs = [1, 2, 3, 4]
        random_num = random.choice(eggs)
        print(f"Here are(is) {random_num} eggs for you")

class AquaticAnimal (Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = abs(dz * self.speed//2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    # super().attack()
    # super().move()
    # super().get_cords()
    # super().dive_in()
    # super().lay_eggs()
    #
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
