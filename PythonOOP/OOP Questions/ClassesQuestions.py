print("\nQ1a\n")


# Q1a: Create a class which of a country (include continent, climate, language etc. in the inputs)

# A1a:
class Country(object):
    def __init__(self, continent, climate, language):
        self.continent = continent
        self.climate = climate
        self.language = language

    def get_continent(self):
        return self.continent

    def get_climate(self):
        return self.climate

    def get_language(self):
        return self.climate


c1 = Country("Europe", "Mild", "English")
print(c1.get_continent())

print("\nQ1b\n")


# Q1b: Create a subclass of a city which inherits from the country class

# A1b:
class City(Country):
    def __init__(self, continent, climate, language):
        super().__init__(continent, climate, language)

# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")

# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    return False
            return True
        else:
            return False

    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False


# A2a:
new_list = []
for num in list_of_numbers:
    if Number(num).is_prime():
        new_list.append(num)

print(new_list)

# print("\nQ2b\n")
# # Q2b: Now create a list of numbers from list_of_numbers that are divisible
# # by both 3 and 4 using the divisible_by_n method above
#
# # A2b:
#
#
# # -------------------------------------------------------------------------------------- #
#
# print("\nQ3a\n")
# # Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)
#
#
# # class Boss(object):
# #     def __init__(self, name, attitude, behaviour, face):
# #         name = name
# #         attitude = attitude
# #         behaviour = behaviour
# #         face = face
# #
# #     def get_attitude(self):
# #         return attitude
# #
# #     def get_behaviour(self):
# #         return behaviour
# #
# #     def get_face(self):
# #         return face
# #
# #
# # class GoodBoss(Boss):
# #     def __init__(self, name, attitude, behaviour, face):
# #         super()
# #
# #    def encourage(self):
# #        print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")
#
#
# # A3a:
#
#
# # -------------------------------------------------------------------------------------- #
#
