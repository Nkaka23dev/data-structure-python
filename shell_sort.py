'''Find the sum of number between 1 to 5'''


def sum_of_number(n):
    if n == 1:
        return 1
    return n + sum_of_number(n - 1)


if __name__ == '__main__':
    print(sum_of_number(100))