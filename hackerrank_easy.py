def split_and_join(line):
    return "-".join(line.split())


# Taking user input
user_input = input()
print(split_and_join(user_input))
