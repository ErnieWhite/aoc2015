with open('data/day2input.txt', 'r', encoding='utf-8') as f:
    reader = f.readlines()
    papper_needed = 0
    length = 0
    width = 1
    height = 2
    for line in reader:
        cleaned_line = line.strip()
        dimensions = [int(x) for x in cleaned_line.split('x')]
        surface_areas = [
            dimensions[length] * dimensions[width] * 2,
            dimensions[width] * dimensions[height] * 2,
            dimensions[length] * dimensions[height] * 2,
        ]
        # add in the extra papper
        surface_areas.append(min(surface_areas)//2)

        papper_needed += sum(surface_areas)

    print(papper_needed)
