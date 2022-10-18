from pprint import pprint


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


def create_wires(wires, input):
    for _, a1, a2, a3 in iterinput(input):
        for wire_id in (a1, a2, a3):
            if not isinstance(wire_id, str) or wire_id in wires:
                continue

            # id (str)
            # signal (int, None)
            # source (int, str, tuple, None)

            wires[wire_id] = {
                'signal': None,
                'source': None,
                'destination': [],
            }


def connect_wires(wires, input):
    for op, a1, a2, a3 in iterinput(input):
        if op == 'set':
            source, destination = a1, a2

            wires[destination]['source'] = source

            if isinstance(source, str):
                wires[source]['destination'].append(destination)
        elif op == 'not':
            source, destination = a1, a2

            wires[destination]['source'] = (op, source)

            if isinstance(source, str):
                wires[source]['destination'].append(destination)
        elif op in ('or', 'and', 'rshift', 'lshift'):
            left, right, destination = a1, a2, a3

            wires[destination]['source'] = (op, left, right)

            if isinstance(left, str):
                wires[left]['destination'].append(destination)

            if isinstance(right, str):
                wires[right]['destination'].append(destination)
        else:
            raise NotImplementedError(f'Unhandled op "{op}"')


def power_on(wires):
    for wire_id, wire in wires.items():
        source = wire['source']

        if isinstance(source, int):
            wire['signal'] = source

            print(wire)


def level_1(input):
    wires = {}

    # Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0
    # to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each
    # wire can only get a signal from one source, but can provide its signal to multiple destinations.
    # A gate provides no signal until all of its inputs have a signal.

    create_wires(wires, input)
    connect_wires(wires, input)
    power_on(wires)

    # pprint(wires)

    # return wires['a']['signal']
