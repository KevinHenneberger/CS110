"""
OOP
- Procedural programming vs. Object Oriented Programming (OOP)
- higher level of abstraction
- write module code
- Object = noun (person, place, or thing)
    - has attributes and a state
    - has behaviors
- Class = blueprint
"""

import microwave
import popcorn

def main():

    my_microwave = microwave.Microwave()
    my_popcorn = popcorn.Popcorn()

    my_microwave.setTime(2.0)
    my_microwave.addFood(my_popcorn)
    my_microwave.cook()

main()

class Superhero:

    name = ""
    powers = ""

    def saveTheDay():
        pass

def main():

    ironman = superhero.Superhero()
    captain_america = superhero.Superhero()

    ironman.setPowers()
    ironman.saveTheDay()

    captain_america.setPowers()
    captain_america.saveTheDay()

main()
