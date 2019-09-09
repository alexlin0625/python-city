def draw_park(population):
    if population > 500:
        length = 90
        width = 60
    elif population > 2500:
        length = 180
        width = 120
    else:
        length = 45
        width = 30

    compute_area(length, width)
    draw_length_park(length)
    draw_width_park(width)


def compute_area(length, width):
    return length*width


def draw_length_park(length):
    for _ in range(length):
        print(".", end="")
    print()


def draw_width_park(width):
    for _ in range(width):
        print("|", end="")


draw_park(50)

