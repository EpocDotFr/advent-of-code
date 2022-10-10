class Day1:
    @staticmethod
    def level_1(input):
        up_count = input.count('(')
        down_count = input.count(')')

        return up_count - down_count

    @staticmethod
    def level_2(input):
        floor = 0

        for p, c in enumerate(input):
            if c == '(':
                floor += 1
            else:
                floor -= 1

            if floor == -1:
                return p + 1

        return ''


class Day2:
    @staticmethod
    def iter_input(input):
        for box in input.splitlines():
            yield [int(d) for d in box.strip().split('x')]

    @staticmethod
    def level_1(input):
        computed = []

        for l, w, h in Day2.iter_input(input):
            computed.append(
                2 * l * w + 2 * w * h + 2 * h * l + min([l * w, w * h, h * l])
            )

        return sum(computed)

    @staticmethod
    def level_2(input):
        computed = []

        for l, w, h in Day2.iter_input(input):
            d = [l, w, h]

            lowest_1 = min(d)

            d.remove(lowest_1)

            lowest_2 = min(d)

            computed.append(
                2 * lowest_1 + 2 * lowest_2 + l * w * h
            )

        return sum(computed)
