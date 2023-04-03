# 3-1 Names
names = ["sandy", "DeLana", "Jerry", "thomas", "Jackson"]
print(names)
print(names[0])
print("")

# 3-1 Greetings
print(f"Hello, {names[1]}")
print(f"Hello, {names[3].title()}!")
print("")

# 3-3 my own list
my_harleys = ["bad boy", "V-Rod", "XR 1200", "road glide"]
print(f"My first H-D motorcycle was a 1998 {my_harleys[0].title()}")
print(f"My favorite touring bike is a  {my_harleys[-1].title()}")
print("")

# 3-4 Guest List
dinner_guests = ["Jesus", "Richard Yates Quinn", "DeLana"]
print(f"My Lord and Savior {dinner_guests[0]}, - could you bless me by attending dinner?")
print(f"I have a special guest I would like for you to meet in person, {dinner_guests[1]}")
print(f"{dinner_guests[-1]}, you won't believe who we will be dining with tonight")
print(f"{dinner_guests[0]}, is unable to attend the dinner")
print("")

# 3-5 Changing the list
dinner_guests = ["Yoda", "Richard Yates Quinn", "DeLana"]
print(f"{dinner_guests[0]}, - could you possibly coach us by attending dinner?")
print(f"I am pleased to annouce we lave a larger table for our soecial'dinner with Yoda")
print("")

# 3-6 More Guests
dinner_guests.insert(1, "Jearldean")
dinner_guests.insert(3, "Thomas")
dinner_guests.insert(-2, "Jackson")
print(dinner_guests)
print(f"{dinner_guests[1]}, can you join as at out expanded table for dinner?")
# print(f"{dinner_guests[3]}, can you join as at out expanded table for dinner?")
# print(f"{dinner_guests[-2]}, can you join as at out expanded table for dinner?")
print("")
# 3-7 Shrinking Guest List
print(dinner_guests)
print(f"Oh no!, the larger table did not arrive on time so only have for two guests")
print("")
"""   cannot put a line break in this print statement 
print("I regret to inform you that we were downgraded to a much smaller \n
       so you will not be able to join us for the dinner")

      need help with line break ----------"""

print(f"{dinner_guests[2]}, I'm sorry, but no room at the table")
dinner_guests.pop(2)
print(dinner_guests)
print(f"{dinner_guests[-1]}, I'm sorry, but no room at the table")
dinner_guests.pop(-1)
print(dinner_guests)
print(f"{dinner_guests[1]}, I'm sorry, but no room at the table")
dinner_guests.pop(1)
print(dinner_guests)
print(f"{dinner_guests[-1]}, I'm sorry, but no room at the table")
dinner_guests.pop(-1)
print(dinner_guests)
print(f"{dinner_guests[0]} and {dinner_guests[-1]} are the dinner guests")

print("")
del dinner_guests[0]
del dinner_guests[-1]
print(dinner_guests)

# 3-9
print(f"The total number of dinner guest is {len(dinner_guests)}")
print("")
# 3-8 See the World
see_world_visit = ["Rome", "Granville", "Lynchburg", "Rock City", "Nile"]
print(see_world_visit)
print(sorted(see_world_visit))
print(see_world_visit)
print("")
new_list = sorted(see_world_visit)
print(new_list)
new_list.reverse()
print(new_list)
print("")
new_list.reverse()
print(new_list)
print("")
new_list.reverse()
print(new_list)
print("")
# 3-9
print(f"The number of wish list visits  is {len(new_list)}")
print("")
# 3-10 Every Function
topics = ["fish", "poultry", "beef", "pork ", "vegan"]
print("here is the original list:")
print(topics)
print("\nhere is the sorted list:")
print(sorted(topics))
print("\nhere is the original list again:")
print(topics)
print("")
print(f"the length of both lists is {len(topics)}")

# 3-11 Index Errors
print("I have corrected several index errors")




