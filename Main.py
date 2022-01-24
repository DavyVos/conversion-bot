from MyObject import MyObject


def main():
    tuple_of_my_object = init_my_objects()
    print_my_object(tuple_of_my_object)


def init_my_objects():
    my_tuple = (MyObject(1, "Poopypants"), MyObject(2, "Pablo"))
    return my_tuple


def print_my_object(my_tuple):
    for x in my_tuple:
        print("Name of first object is: " + x.name + "\nHis jersey number is: " + str(x.number))


if __name__ == '__main__':
    main()
