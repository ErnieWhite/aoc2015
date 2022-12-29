with open('data/day2input.txt', 'r', encoding='utf-8') as f:
    reader = f.readlines()
    ribbon_needed = 0
    length = 0
    width = 1
    height = 2
    for line in reader:
        cleaned_line = line.strip()
        dimensions = [int(x) for x in cleaned_line.split('x')]
        perimeters = [
            dimensions[length] * 2 + dimensions[width] * 2,
            dimensions[width] * 2 + dimensions[height] * 2,
            dimensions[length] * 2 + dimensions[height] * 2,
        ]
        ribbon_wrap = min(perimeters)
        ribbon_bow = dimensions[length]*dimensions[width]*dimensions[height]
        ribbon_needed += ribbon_bow + ribbon_wrap

    print(ribbon_needed)
