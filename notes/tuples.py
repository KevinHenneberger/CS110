"""
Tuples
- primarily for records (group data)
- immutable
- lists require a lot of memory and time (expensive)
- can return multiple values from a function
"""

def foo():

    x = 3
    y = 5

    return (x, y)

def main():

    t = (1, 2, 3)
    print(t)

    new_t = t[1:]
    print(new_t)

    car = ("Honda", "Accord", 2017)
    (brand, model, year) = car
    print(brand)
    print(model)
    print(year)
    
    # swapping two values
    temp = year
    year = model
    model = temp

    (year, model) = (model, year)

    (x, y) = foo()

main()
