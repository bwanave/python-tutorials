def print_squares_upto(n):
    for i in range(1, n + 1):
        print(i * i)


def print_squares_of_even_numbers(n):
    for i in range(2, n + 1, 2):
        print(i * i)


def print_numbers_in_reverse_orders(n):
    for i in range(n, 0, -1):
        print(i)


print_squares_upto(10)
print('--------------------------------------')
print_squares_of_even_numbers(10)
print('--------------------------------------')
print_numbers_in_reverse_orders(10)
