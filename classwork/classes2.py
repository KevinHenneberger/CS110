import random

class MainCharacter:

    def __init__(self, name, x, y, skillPoints):
        self.name = name
        self.x = x
        self.y = y
        self.skillPoints = skillPoints

    def move(self, direction):

        if (direction == "up"):
            self.y += self.skillPoints["speed"]
        elif (direction == "down"):
            self.y -= self.skillPoints["speed"]
        elif (direction == "left"):
            self.x -= self.skillPoints["speed"]
        elif (direction == "right"):
            self.x += self.skillPoints["speed"]

    def fight(self, enemy):

        selfMultStrength = random.randrange(10) * self.skillPoints["strength"]
        selfMultSpeed = random.randrange(10) * self.skillPoints["speed"]

        enemyMultStrength = random.randrange(10) * enemy.skillPoints["strength"]
        enemyMultSpeed = random.randrange(10) * enemy.skillPoints["strength"]

        return ((selfMultStrength + selfMultSpeed) > (enemyMultStrength + enemyMultSpeed))

def main():

    hero = MainCharacter("?", 100, 100, {"strength": 8, "speed": 1, "intelligence": 1})
    enemy = MainCharacter("??", 200, 200, {"strength": 4, "speed": 4, "intelligence": 1})

    hero.move("left")
    hero.move("right")
    hero.move("up")
    hero.move("down")

    for t in range(10): 
        if (hero.fight(enemy)):
            print("Success")
        else:
            print("Failure")

main()
