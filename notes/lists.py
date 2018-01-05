def main():

    fruits = ['apple', 'banana', 'watermelon']
    print(fruits)

    for fruit in fruits:
        print(fruit)

    print(len(fruits))

    if ('watermelon' in fruits):
        print('watermelon is in the list')

    # array slicing
    print(fruits[0:2])

    # append element to list
    fruits = fruits + ['orange']
    fruits.append('lime')
    print(fruits)

    # add element to list at index
    fruits[1:1] = ['pineapple']

    # lists are mutable
    fruits[0] = 'strawberry'
    print(fruits)

    # copy of array
    other_fruits = fruits
    other_fruits[0] = 'lemon'
    print(fruits)
    print(other_fruits)

    # make new copy of array
    other_fruits = fruits[:]
    other_fruits[0] = 'apple'
    print(fruits)
    print(other_fruits)

    # delete element
    print(fruits)
    del fruits[1]
    print(fruits)

    # remove the last element
    # returns popped element
    print(fruits)
    print(fruits.pop())
    print(fruits)

    # true
    a = 'hello'
    b = 'hello'
    print(a is b)

    # false
    c = [1, 2, 3]
    d = [1, 2, 3]
    print(c is d)

    mylist = [1, 2, 3]

    for i in range(len(mylist)):
        mylist[i] += 10

    print(mylist)

main()
