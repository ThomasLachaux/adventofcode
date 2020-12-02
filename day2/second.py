import re


with open('input.data', 'r') as file:
    lines = file.readlines()
    passwords = []

    for line in lines:
        regex = re.search(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)', line)

        passwords.append(regex.groups())

    valid = 0
    invalid = 0

    for passwordGroups in passwords:
        firstIndex = int(passwordGroups[0]) - 1
        secondIndex = int(passwordGroups[1]) - 1
        letter = passwordGroups[2]
        password = passwordGroups[3]

        if password[firstIndex] == letter and password[secondIndex] != letter:
            valid += 1

        elif password[firstIndex] != letter and password[secondIndex] == letter:
            valid += 1

        else:
            invalid += 1

    print(valid)
    print(invalid)