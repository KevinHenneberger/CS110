import json

class CustomerData:

    def __init__(self, name, number, dop, cost):
        self.name = name
        self.number = number
        self.dop = dop
        self.cost = cost

    def write_to_json(self):
        cfile = open("data.json", "r")
        cdict = json.load(cfile)
        cfile.close()

        cdict[self.name] = {
            "Phone": self.number, 
            "DOP": self.dop, 
            "Cost": self.cost
        }

        cfile = open("data.json", "w")
        cfile.write(json.dumps(cdict, indent=4))
        cfile.close()

    def __str__(self):
        return "Name: " + self.name + "\nNumber: " + self.number + "\nDOP: " + self.dop + "\nCost: " + str(self.cost)

customer_data = CustomerData("EEEE", "555-5555", "5/55/55", 55.55)
customer_data.write_to_json()
print(customer_data)
