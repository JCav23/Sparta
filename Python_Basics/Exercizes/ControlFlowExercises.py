print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
x_asc = sorted(x)
print(x_asc[0:5])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
even_num = []
for num in x:
    if num % 2 == 0:
        even_num.append(num)
print(even_num)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
even_num = []
for num in x[0:5]:
    if num % 2 == 0:
        even_num.append(num)
print(even_num)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
letters = []
for name in names:
    letters.append(name[0])
print(letters)


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
space_position = []
for name in names:
    space_position.append(name.index(" "))
print(space_position)


print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
initials = []
for name in names:
    initials.append(name[0] + ". " + name[name.index(" ")+1])
print(initials)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:
set_list = []
for l in list_of_lists:
    set_list.append(set(l))

no_duplicates = []
for s in set_list:
    len(s)
    for l in list_of_lists:
        if len(s) == len(l):
            no_duplicates.append(l)

print(no_duplicates)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
pick_number = True

while pick_number:
    player_choice = int(input("Please enter a number over 100: "))
    if player_choice <= 100:
        print("Number too low, please try again")
    elif player_choice > 100:
        print (f"{player_choice} is over 100, you win")
        pick_number = False

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
pick_number = True

while pick_number:
    player_choice = int(input("Please enter a number over 100: "))
    is_prime = True
    if player_choice <= 100:
        print("Number too low, please try again")
        if player_choice == 1:
            is_prime = False
        elif player_choice > 1:
            for num in range(2, player_choice):
                if player_choice % num == 0:
                    is_prime = False
            if is_prime:
                print(player_choice, "is prime")
            else:
                print(player_choice, "is not prime")
    elif player_choice > 100:
        print(f"{player_choice} is over 100, you win")
        if player_choice > 100:
            for num in range(2, player_choice):
                if player_choice % num == 0:
                    is_prime = False
            if is_prime:
                print(player_choice, "is prime")
            else:
                print(player_choice, "is not prime")
        pick_number = False







