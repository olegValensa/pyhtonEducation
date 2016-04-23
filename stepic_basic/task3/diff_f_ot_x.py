def some_value(x):
    if x <= -2:
        return 1 - (x + 2) * (x + 2)
    elif -2 < x <= 2:
        return - x / 2
    elif x > 2:
        return (x - 2) * (x - 2) + 1

print(some_value(1))
