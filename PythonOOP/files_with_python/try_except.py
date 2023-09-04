try:
    with open("order.txt") as file:
    # file = open("order.txt", "r")
        file_line_list = file.readlines()
        for line in file_line_list:
            line = line.split(',')
            for word in line:
                print(word.strip())
    # file.close()
except FileNotFoundError as msg:
    print("There has been an error! panic")
    print(msg)
    raise
except SyntaxError:
    print("error")