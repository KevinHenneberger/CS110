def main():

    a = [1, 2, 3]
    print(a)

    a.append('apple')
    a.append(76)
    a[0:1] = [99]
    print(a)

    a.remove(76)
    print(a)

    for i in range(len(a)):
        if (a[i] == 'apple'):
            a[i] = 'orange'

    print(a)

main()
