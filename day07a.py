with open('data/day7input.txt', encoding='utf-8', newline='') as f:
    program = f.readlines()
    wires = {}
    for line in program:
        line = line.strip()
        tokens = line.split()
        if 'AND' in tokens:
            a = int(tokens[0]) if tokens[0].isdigit() else wires.get(tokens[0], 0)
            b = int(tokens[2]) if tokens[2].isdigit() else wires.get(tokens[2], 0)
            wires[tokens[4]] = a & b
        elif 'OR' in tokens:
            a = int(tokens[0]) if tokens[0].isdigit() else wires.get(tokens[0], 0)
            b = int(tokens[2]) if tokens[2].isdigit() else wires.get(tokens[2], 0)
            wires[tokens[4]] = a | b
        elif 'NOT' in tokens:
            a = int(tokens[1]) if tokens[1].isdigit() else wires.get(tokens[1], 0)
            wires[tokens[3]] = ~a
        elif 'LSHIFT' in tokens:
            a = int(tokens[0]) if tokens[0].isdigit() else wires.get(tokens[0], 0)
            b = int(tokens[2]) if tokens[2].isdigit() else wires.get(tokens[2], 0)
            wires[tokens[4]] = a << b
        elif 'RSHIFT' in tokens:
            a = int(tokens[0]) if tokens[0].isdigit() else wires.get(tokens[0], 0)
            b = int(tokens[2]) if tokens[2].isdigit() else wires.get(tokens[2], 0)
            wires[tokens[4]] = a >> b
        else:
            a = int(tokens[0]) if tokens[0].isdigit() else wires.get(tokens[0], 0)
            wires[tokens[2]] = a
    for k, v in wires.items():
        print(f'{k:2}: {v}')

    print(f'a: {wires["a"]}')
