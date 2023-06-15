"""   --- ignore for now --- """
print("Ex 5_1 Conditional Tests")
car1 = 'Ford'
car2 = 'Infiniti'

print("Is car1 ==  'Ford'? I predict True")
print(car1 == 'Ford')

print("\nIs car1 ==  'Chevy'? I predict False")
print(car2 == 'Chevy')

print("\nIs car2 ==  'Infiniti'? I predict True")
print(car2 == 'Infiniti')

print("\nIs car2 ==  'infiniti'? I predict False")
print(car2 == 'infiniti')

print("\nEx 5_2 More Conditional Tests")

car2.lower() ==  'infiniti'
print(car2.lower())
print("Is car2.lower() == 'infiniti'? I predict True")
print(car2.lower() == 'infiniti')

str1 = "gh23"
str2 = "gh33"
print("\nIs str2 ==  'gh23'? I predict False")
print(str2 == 'gh23')

print("\nIs str2 ==  'gh23' or str1 == 'gh23'? I predict True")
print(str2 ==  'gh23' or str1 == 'gh23')

print("\nIs str2 ==  'gh23' and str1 == 'gh23'? I predict False")
print(str2 ==  'gh23' and str1 == 'gh23')


print("\nIs str1 ==  'gh23'? I predict True")
print(str1 == 'gh23')

print("\nIs (3 + 1) ==  (2 + 2) ? I predict True")
print((3 + 1) ==  (2 + 2))

print("\nIs (3 + 1) >=  4 ? I predict True")
print((3 + 1) >= 4)

print("\nIs (3 + 1) <=  2 ? I predict True")
print((3 + 1) <= 2)

print("\nIs (3 + 1) <=  5 ? I predict False")
print((3 + 1) <= 2)


"""
need to run this in terminal
car1 = 'Ford'
car2 = 'Infiniti'
my_cars = [car1, car2]
'Ford' in my_cars #True

'ford' in my_cars #False
"""

print("\nEx 5_3 Alien Colors_1")
alien_color = 'green'
if alien_color == 'green':  #I predict the 5 point message
    print("You earned 5 points")

if alien_color != 'green': #I pedit no output
    pass

print("\nEx 5_4 Alien Colors_2")
alien_color = 'green'  # i predict 5 points
# alien_color = 'yellow"
if alien_color == 'green':  #I predict the 5 point message
    print("You earned 5 points")
else:
    print("You earned 10 points")

alien_color = 'yellow' # I predict 10 points
if alien_color == 'green':
    print("You earned 5 points")
else:
    print("You earned 10 points")


print("\nEx 5_5 Alien Colors #3")
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points")
elif alien_color != 'green':
    print("You earned 10 points")

alien_color = 'yellow' # I predict 10 points
if alien_color == 'green':  #I predict the 5 point message
    print("You earned 5 points")
elif alien_color != 'green':
    print("You earned 10 points")

print("\nEx 5_6 Stages of Life")
# variable_age = 1
variable_age = 70
if variable_age < 2:
    print("You are a baby")
elif variable_age >= 2 and variable_age < 4:
     print("You are a toddler")
elif variable_age  >= 4 and variable_age < 13:
     print("You are a kid")
elif variable_age >= 13 and variable_age < 20:
     print("You are a teenager")
elif variable_age >= 20 and variable_age < 65:
     print("You are an adult")
else:
    print("You are an elder")

print("\nEx 5_7 Favorite Fruits")
favorite_fruits = ["bananas",   "grapes",    "oranges"]
test_fruit = "apples"  # predit it will NOT print
if "test_fruit" in favorite_fruits:
    print("You do like ", test_fruit)

test_fruit = "grapes"  # predit it will print
if "grapes" in favorite_fruits:
    print("You do like ", test_fruit)

test_fruit = "plums"  # predit it will NOT print
if "plums" in favorite_fruits:
    print("You do like ", test_fruit)

test_fruit = "oranges"  # predict it will print
if "oranges" in favorite_fruits:
    print("You do like ", test_fruit)

test_fruit = "bananas"  # predit it will print
if "bananas" in favorite_fruits:
    print("You do like ", test_fruit)


print("\nEx 5_8 Hello Admin")
usernames = ["quinnrs", "admin", "jerry", "delana", "thomas"]
for username in usernames:
    if username == "admin":
        print(f'Hello, {username}, would you like to see a status report?')
    else:
        print(f'Hello, {username}, welcome back')

print("what next?")

print("\nEx 5_9 No users (empty lists)")
# usernames = []  # predict empty list message
if username not in usernames: # predict personalized message
    print("we need to find some users")
for username in usernames:
    if username == "admin":
        print(f'Hello, {username}, would you like to see a status report?')
    elif username != "admin":
        print(f'Hello, {username}, welcome back')

print("\nEx 5_10 Checking Usernames")
current_users = ["quinnrs", "admin", "Jerry", "DeLana", "thomas"]
users_test_list = []
for current_user in current_users:
    users_test_list.append(current_user.lower())
print(users_test_list)
# current_users.lower()
# usernames = ["quinnrs", "admin", "jerry", "delana", "thomas"]
new_users = ["Jackson",  "Nicole", "Thomas", "peter", "jerry"]
# predict Thomas and jerry will not be available
for new_user in new_users:
    print(new_user)
    # print(new_user.lower())
    if new_user in users_test_list or new_user.lower() in users_test_list:
    # if new_user in users_test_list:
    # if new_user.lower() in users_test_list:
        print("That name is not available, please enter another user name.")
    else:
        print("that user  name is available")


print("\nEx 5_11 Ordinal Numders")
# number_strings = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(str(number)+"st")
    elif number == 2:
        print(str(number)+"nd")
    elif number == 3:
        print(str(number)+"rd")
    elif number >= 4:
        # print(number,"th") this prints 4 th - don't want the space
        print(str(number)+"th")

print("\nEx 5_12 Styling & Future Ideas")
print("done")