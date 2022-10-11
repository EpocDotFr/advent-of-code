def iter_input(input):
    for box in input.splitlines():
        yield [int(d) for d in box.strip().split('x')]


def level_1(input):
    computed = []

    for l, w, h in iter_input(input):
        computed.append(
            2 * l * w + 2 * w * h + 2 * h * l + min([l * w, w * h, h * l])
        )

    return sum(computed)


def level_2(input):
    computed = []

    for l, w, h in iter_input(input):
        d = [l, w, h]

        lowest_1 = min(d)

        d.remove(lowest_1)

        lowest_2 = min(d)

        computed.append(
            2 * lowest_1 + 2 * lowest_2 + l * w * h
        )

    return sum(computed)
