def sum_of_squares(x):
    if x == 1:
        return 1
    else:
        return x * x + sum_of_squares(x - 1)


print(sum_of_squares(3))

