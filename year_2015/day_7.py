def str2int(value):
    return int(value) if value.isdecimal() else value


def iterinstructions(input):
    for instruction in input.splitlines():
        operation, destination = instruction.split(' -> ', maxsplit=1)
        destination = str2int(destination)

        operation_parts = operation.split(' ')

        if len(operation_parts) == 1:
            value, = operation_parts
            value = str2int(value)

            yield 'set', value, destination, None
        elif len(operation_parts) == 2:
            gate, source = operation_parts
            gate = gate.lower()
            source = str2int(source)

            yield gate, source, destination, None
        elif len(operation_parts) == 3:
            left, gate, right = operation_parts
            gate = gate.lower()
            left, right = str2int(left), str2int(right)

            yield gate, left, right, destination


def level_1(input):
    circuit = {}

    for op, a1, a2, a3 in iterinstructions(input):
        print(op, a1, a2, a3)

        result = 0

        if op == 'set':
            value, destination = a1, a2

            result = value
        elif op == 'not':
            source, destination = a1, a2
        else:
            left, right, destination = a1, a2, a3

        circuit[destination] = result

    exit()
