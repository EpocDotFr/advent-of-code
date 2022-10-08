from support import advent_of_code
import importlib
import argparse


def run():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('year', type=int, choices=list(range(2015, 2022)))
    arg_parser.add_argument('day', type=int, choices=list(range(1, 26)))
    arg_parser.add_argument('level', type=int, default=1, nargs='?', choices=[1, 2])

    args = arg_parser.parse_args()

    try:
        year_module = importlib.import_module(f'year_{args.year}')
    except ImportError:
        print(f'Year not available yet: {args.year}')

        exit()

    try:
        day_class = getattr(year_module, f'Day{args.day}')
    except AttributeError:
        print(f'Day not available yet: {args.day}')

        exit()

    try:
        level_method = getattr(day_class, f'level_{args.level}')
    except AttributeError:
        print(f'Level not available yet: {args.level}')

        exit()

    puzzle = advent_of_code.Puzzle(args.year, args.day)

    input = puzzle.fetch()

    answer = level_method(input)

    print(puzzle.answer(answer, args.level))


if __name__ == '__main__':
    run()
