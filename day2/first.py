import re


with open('input.data', 'r') as file:
    lines = file.readlines()
    passwords = []

    for line in lines:
        regex = re.search(r'^(\d+)-(\d+) ([a-z]): ([a-z]+)', line)

        passwords.append(regex.groups())

    valid = 0
    invalid = 0

    for password in passwords:
        count = password[3].count(password[2])

        if count >= int(password[0]) and count <= int(password[1]):
            valid += 1

        else:
            invalid += 1

    print(valid)
    print(invalid)