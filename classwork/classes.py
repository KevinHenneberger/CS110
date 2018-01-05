import time

class RescueAnimal:

    def __init__(self, id, name, type="dog", arrivalDate=time.strftime("%m/%d/%Y"), adoptionDate=time.strftime("%m/%d/%Y")):
        self.id = id
        self.name = name
        self.type = type
        self.arrivalDate = arrivalDate
        self.adoptionDate = adoptionDate

    def setAdoptionDate(self, date):
        self.adoptionDate = date

    def __str__(self):
        return "[" + str(self.id) + ", " + self.name + ", " + self.type + ", " + self.arrivalDate + ", " + self.adoptionDate  + "]"

rescueDog = RescueAnimal(1, "Snoopy")
rescueDog.setAdoptionDate("04/1/2017")
print(rescueDog)

rescueCat = RescueAnimal(2, "Tom", "cat")
rescueCat.setAdoptionDate("04/5/2017")
print(rescueCat)
