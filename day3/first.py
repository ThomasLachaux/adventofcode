with open('input.data', 'r') as file:
    lines = file.readlines()

    x = 0
    y = 0

    trees = 0
    dots = 0

    width = len(lines[0]) - 1
    height = len(lines)

    while y < height:
        print("x: {} y: {}".format(x, y))
        if lines[y][x] == '#':
            trees += 1
        
        elif lines[y][x] == '.':
            dots += 1

        x += 3
        x %= width
        y += 1

    print('{} trees. {} dots'.format(trees, dots))