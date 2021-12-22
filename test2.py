def test5():
    input_data = input()

    input_list_test = input_data.split(" ")
    input_list_test = list(map(int, input_list_test))

    return input_list_test


def main():
    list1 = test5()

    for i in range(9):
        print(list1[i], end=' ')
        if (i + 1) % 3 == 0:
            print()


if __name__ == '__main__':
    main()
