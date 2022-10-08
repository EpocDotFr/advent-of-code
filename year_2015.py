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
