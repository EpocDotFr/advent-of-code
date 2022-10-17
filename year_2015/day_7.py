def str2int(value):
    return int(value) if value.isdecimal() else value


def iterinput(input):
    for instruction in input.splitlines():
        operation, destination = instruction.split(' -> ', maxsplit=1)
        destination = str2int(destination)

        operation_parts = operation.split(' ')

        if len(operation_parts) == 1:
            value, = operation_parts
            value = str2int(value)

            yield 'set', value, destination, None
        elif len(operation_parts) == 2:
            op, source = operation_parts
            op = op.lower()
            source = str2int(source)

            yield op, source, destination, None
        elif len(operation_parts) == 3:
            left, op, right = operation_parts
            op = op.lower()
            left, right = str2int(left), str2int(right)

            yield op, left, right, destination


def level_1(input):
    for op, a1, a2, a3 in iterinput(input):
        print(op, a1, a2, a3)

        if op == 'set':
            value, destination = a1, a2
        elif op == 'not':
            source, destination = a1, a2
        else:
            left, right, destination = a1, a2, a3

    exit()
