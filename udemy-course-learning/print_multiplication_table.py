def print_multiplication_table(table=5, start=1, end=20):
    for i in range(start, end + 1):
        print(f"{table} x {i} = {table * i}")


print_multiplication_table()
print("----------------")
print_multiplication_table(4)
print("----------------")
print_multiplication_table(10, 1, 10)
