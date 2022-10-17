def turn(grid, state, pos1, pos2):
    for pos in iterpos(pos1, pos2):
        grid[pos] = state


def toggle(grid, pos1, pos2):
    for pos in iterpos(pos1, pos2):
        grid[pos] = not grid[pos] if pos in grid else True


def brigthness(grid, factor, pos1, pos2):
    for pos in iterpos(pos1, pos2):
        if pos not in grid:
            grid[pos] = 0

        grid[pos] += factor

        if grid[pos] <= 0:
            grid[pos] = 0


def iterpos(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            yield x, y


def iterinput(input):
    for instruction in input.splitlines():
        instruction = instruction.replace('turn', '').replace(' through ', '-').strip()

        action, positions = instruction.split(' ', maxsplit=1)

        pos1, pos2 = [[int(p) for p in pos.split(',')] for pos in positions.split('-')]

        yield action, pos1, pos2


def level_1(input):
    grid = {}

    for action, pos1, pos2 in iterinput(input):
        if action == 'on':
            turn(grid, True, pos1, pos2)
        elif action == 'off':
            turn(grid, False, pos1, pos2)
        elif action == 'toggle':
            toggle(grid, pos1, pos2)

    return sum([
        1 for state in grid.values() if state is True
    ])


def level_2(input):
    grid = {}

    for action, pos1, pos2 in iterinput(input):
        if action == 'on':
            brigthness(grid, +1, pos1, pos2)
        elif action == 'off':
            brigthness(grid, -1, pos1, pos2)
        elif action == 'toggle':
            brigthness(grid, +2, pos1, pos2)

    return sum(grid.values())
