with open('input.data', 'r') as file:
    lines = file.readlines()

    total = 1

    for (stepX, stepY) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        print("x: {} y: {}".format(stepX, stepY))
        x = 0
        y = 0

        trees = 0
        dots = 0

        width = len(lines[0]) - 1
        height = len(lines)

        while y < height:
            if lines[y][x] == '#':
                trees += 1
            
            elif lines[y][x] == '.':
                dots += 1

            else:
                print("Invalid character {}".format(lines[y][x]))

            x += stepX
            x %= width
            y += stepY

        total *= trees

        print('{} trees. {} dots'.format(trees, dots))

    print('Total {}'.format(total))