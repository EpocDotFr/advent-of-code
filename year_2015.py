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
    def level_1(input):
        computed = []

        for box in input.splitlines():
            l, w, h = [int(d) for d in box.strip().split('x')]

            computed.append(
                2 * l * w + 2 * w * h + 2 * h * l
            )

        return sum(computed)

    @staticmethod
    def level_2(input):
        return ''
