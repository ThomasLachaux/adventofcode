
with open('input.data', 'r') as file:
    numbers = file.readlines()

    numbers = list(map((lambda x: x[:-1]), numbers))

    yo = []
    for a in numbers:
        for b in numbers:
            for c in numbers:
                result = int(a) + int(b) + int(c)

                if result == 2020:
                    print("result")
                    print(a)
                    print(b)
                    print(c)