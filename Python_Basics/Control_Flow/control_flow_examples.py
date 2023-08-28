# Control flow examples

"""
Cinema system age management
1. if someone is under 12 - U, PG and 12 films are available
2. if someone is under 15 - U, PG, 12, 15 films are available
3. Over 18 0 all films are available
"""

customer_age = 15

if customer_age < 12:
    print('U, PG and 12 films are available')
elif customer_age <= 15:
    print('U, PG, 12, 15 films are available')
else:
    print('All films are available')

"""
Chatbot greetings
1. between 05:00-12:00 - Good Morning
2. between 12:00-18:00 - Good Afternoon
3. between 18:00-04:59 - Good Evening
"""

time_of_day = 19

# Or & And

if time_of_day > 5 and time_of_day < 12:
    print('Good Morning')
elif time_of_day >12 and time_of_day < 18:
    print('Good Afternoon')
else:
    print('Good Evening')