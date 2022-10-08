class Day1:
    @staticmethod
    def level_1(input):
        up_count = input.count('(')
        down_count = input.count(')')

        return up_count - down_count

    @staticmethod
    def level_2(input):
        return ''
