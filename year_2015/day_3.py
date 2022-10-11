def level_1(input):
    houses = [
        (0, 0)
    ]

    x, y = 0, 0

    for d in input:
        if d == '^':
            y -= 1
        elif d == '>':
            x += 1
        elif d == 'v':
            y += 1
        elif d == '<':
            x -= 1

        pos = (x, y)

        if pos not in houses:
            houses.append(pos)

    return len(houses)


def level_2(input):
    houses = [
        (0, 0)
    ]

    xs, ys, xr, yr = 0, 0, 0, 0

    santa = True

    for d in input:
        if d == '^':
            if santa:
                ys -= 1
            else:
                yr -= 1
        elif d == '>':
            if santa:
                xs += 1
            else:
                xr += 1
        elif d == 'v':
            if santa:
                ys += 1
            else:
                yr += 1
        elif d == '<':
            if santa:
                xs -= 1
            else:
                xr -= 1

        if santa:
            pos = (xs, ys)
        else:
            pos = (xr, yr)

        if pos not in houses:
            houses.append(pos)

        santa = False if santa else True

    return len(houses)
