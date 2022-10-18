import copy


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

            wires[wire_id] = {
                'signal': None,
                'source': None,
                'destinations': [],
            }


def connect_wires(wires, input):
    for op, a1, a2, a3 in iterinput(input):
        if op == 'set':
            source, destination = a1, a2

            wires[destination]['source'] = source

            if isinstance(source, str):
                wires[source]['destinations'].append(destination)
        elif op == 'not':
            source, destination = a1, a2

            wires[destination]['source'] = (op, source, None)

            if isinstance(source, str):
                wires[source]['destinations'].append(destination)
        elif op in ('or', 'and', 'rshift', 'lshift'):
            left, right, destination = a1, a2, a3

            wires[destination]['source'] = (op, left, right)

            if isinstance(left, str):
                wires[left]['destinations'].append(destination)

            if isinstance(right, str):
                wires[right]['destinations'].append(destination)
        else:
            raise NotImplementedError(f'Unhandled op "{op}"')


def power_on(wires):
    for wire_id, wire in wires.items():
        source = wire['source']

        if isinstance(source, int):
            wire['signal'] = source

            power_on_tree(wires, wire)


def power_on_tree(wires, wire):
    for wire_id in wire['destinations']:
        destination_wire = wires[wire_id]

        if destination_wire['signal'] is None:
            signal = None

            if isinstance(destination_wire['source'], str):
                source_wire_signal = wires[destination_wire['source']]['signal']

                if source_wire_signal is not None:
                    signal = source_wire_signal
            else:
                op, a1, a2 = destination_wire['source']

                if op == 'not':
                    source_wire_signal = wires[a1]['signal'] if isinstance(a1, str) else a1

                    if source_wire_signal is not None:
                        signal = ~ source_wire_signal
                elif op == 'rshift':
                    source_wire_signal_left = wires[a1]['signal'] if isinstance(a1, str) else a1
                    source_wire_signal_right = wires[a2]['signal'] if isinstance(a2, str) else a2

                    if source_wire_signal_left is not None and source_wire_signal_right is not None:
                        signal = source_wire_signal_left >> source_wire_signal_right
                elif op == 'lshift':
                    source_wire_signal_left = wires[a1]['signal'] if isinstance(a1, str) else a1
                    source_wire_signal_right = wires[a2]['signal'] if isinstance(a2, str) else a2

                    if source_wire_signal_left is not None and source_wire_signal_right is not None:
                        signal = source_wire_signal_left << source_wire_signal_right
                elif op == 'or':
                    source_wire_signal_left = wires[a1]['signal'] if isinstance(a1, str) else a1
                    source_wire_signal_right = wires[a2]['signal'] if isinstance(a2, str) else a2

                    if source_wire_signal_left is not None and source_wire_signal_right is not None:
                        signal = source_wire_signal_left | source_wire_signal_right
                elif op == 'and':
                    source_wire_signal_left = wires[a1]['signal'] if isinstance(a1, str) else a1
                    source_wire_signal_right = wires[a2]['signal'] if isinstance(a2, str) else a2

                    if source_wire_signal_left is not None and source_wire_signal_right is not None:
                        signal = source_wire_signal_left & source_wire_signal_right
                else:
                    raise NotImplementedError(f'Unhandled op "{op}"')

            if signal is not None:
                destination_wire['signal'] = signal

                power_on_tree(wires, destination_wire)


def level_1(input):
    wires = {}

    create_wires(wires, input)
    connect_wires(wires, input)
    power_on(wires)

    return wires['a']['signal']


def level_2(input):
    wires_1 = {}

    create_wires(wires_1, input)
    connect_wires(wires_1, input)

    wires_2 = copy.deepcopy(wires_1)

    power_on(wires_1)

    old_a_signal = wires_1['a']['signal']

    wires_2['b']['source'] = old_a_signal

    power_on(wires_2)

    return wires_2['a']['signal']
