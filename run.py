from support import advent_of_code
import importlib
import argparse


def run():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('year', type=int)
    arg_parser.add_argument('day', type=int)
    arg_parser.add_argument('level', type=int, default=1, nargs='?')

    args = arg_parser.parse_args()

    year_module = importlib.import_module(f'year_{args.year}')
    day_class = getattr(year_module, f'Day{args.day}')
    level_method = getattr(day_class, f'level_{args.level}')

    puzzle = advent_of_code.Puzzle(args.year, args.day)

    input = puzzle.fetch()

    answer = level_method(input)

    print(puzzle.answer(answer, args.level))


if __name__ == '__main__':
    run()
