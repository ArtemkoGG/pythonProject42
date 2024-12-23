with open("data.txt", "r") as file:
    line = max(file, len)
    print(line, len(line))