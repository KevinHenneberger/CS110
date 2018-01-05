def my_count(my_list):

    l = 0

    for i in my_list:
        l += 1

    return l

def my_sum(data):

    s = 0

    for i in data:
        s += i

    return s

def main():
    print(my_count(['a', 'b', 'c', 'd']))
    print(my_sum(range(10)))
    
main()
