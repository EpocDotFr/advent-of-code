from support import advent_of_code

puzzle = advent_of_code.Puzzle(2015, 1)

input = puzzle.fetch()

up_count = input.count('(')
down_count = input.count(')')

answer = up_count - down_count

print(puzzle.answer(1, answer))
