def level_1(input):
    characters_strings = 0
    characters_memory = 0

    for line in input.splitlines():
        characters_strings += len(line)
        characters_memory += len(eval(line))

    return characters_strings - characters_memory
