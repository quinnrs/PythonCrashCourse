print("Ex 4-1")
pizza_types = ["cheese", "veggie" , "Italian sausage"]
for pizza in pizza_types:
    # print(pizza)
    print(f"You cannot go wrong with, {pizza} pizza")
print(f"I enjoy {pizza_types[0]} pizza")
print(f"I enjoy {pizza_types[1]} pizza a little more")
print(f"I reall enjoy {pizza_types[2]} pizza even more")
print("I never tasted any pizza that I didn't like")

print("\nEx 4-2")
animals =["dog", "cat", "hampster"]
for animal in animals:
    print(animal)
print(f"A {animals[0]} makes a great pet, but need lots of attention")
print(f"A {animals[1]} is more independent and can be alone for extended periods")
print(f"A {animals[0]} is somewhere between a dog or cat for attention required")
print("\nAny of these would be be a great pet")

print("\nEx 4-3")
for value in range(1,21):
    print(value)

print("\nEx 4-4")
one_million = list(range(1, 1000000))
# print(one_million)

print("\nEx 4-5")
print(min(one_million))
print(max(one_million))
print(f"The sum of the numbers in [one_million] is {sum(one_million)}")

print("\nEx 4-6")
odds_20 = list(range(1, 20, 2))
for item in odds_20:
    print(item)

print("\nEx 4-7")
threes_multiple = list(range(3, 30, 3))
for item in threes_multiple:
    print(item)

print("\nEx 4-8")
cubes =[]
for item in range(1, 10):
    # cubes.append(value**3)
    value = item**3
    print(value)

print("\nEx 4-9")
for value in range(1, 10):
    cubes.append(value**3)
    value = item**3
print(f"cubes = {cubes}")

print("\nEx 4-10")
cubes = [1, 8, 27, 64, 125, 216, 343, 512, 729]
print(f"The first three items in cubes are {cubes[:3]}")
print(f"Three items ifrom the middleo  cubes are {cubes[2:5]}")
print(f"The last three items in cubes are {cubes[-3:]}")

print("\nEx 4-11")
pizza_types = ["cheese", "veggie" , "Italian sausage"]
friend_pizzas = pizza_types[:]
pizza_types.append("deluxe")
print(f"pizza_types = {pizza_types}")
friend_pizzas.append("supremo")
print(f"friend_pizzas = {friend_pizzas}")

print("\nEx 4-12")
for n in range(0, len(pizza_types)):
    print(f"pizza types include {pizza_types[n]}")
print("")
for n in range(0, len(pizza_types)):
    print(f"friend_pizzas include {friend_pizzas[n]}")

print("\nEx 4-13")
buffet_menu = ("fish", "carrots" ,"lettuce", "bread", "chicken")
print("The buffet menu is:")
for item in (buffet_menu):
    print(item)
# buffet_menu[0] = "filet_mignon"
buffet_menu = ("filet_mignon", "carrots" ,"lettuce", "bread", "pork")
print("\nThe revised menu is:")
for item in (buffet_menu):
    print(item)

print("\nEx 4-14 and 15")
print("some previous code was editied to comply with PEP 8")