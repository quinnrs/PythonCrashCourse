#2-1 simple_greeting.py
greeting = "Hi, y'all!"
print(greeting)

#2-2 simple_messages.py
msg = ("I'm learning to use Python")
print(msg)
msg = "My daughter is coaching me"
print(msg)

#2-3 personal_msg.py
first_name = "'lana"
last_name = "quinn"
full_name =f"{first_name} {last_name}"
message = f"I love you, {full_name.title()}!"
print(message)

#2-4 name_cases.py
name = "DeLana Quinn"
print(name.upper())
print(name.lower())
print(name.title())

#2-5 famous_quote.py
quote = "I didn't come here, so I ain't leaving"
author = "Willie Nelson"
# print(f"{author} once said, {quote}") #problem with quotes
print("Willie Nelson once said, 'I did not come here")
print("so I ain't leaving'")
#2-6 famous_quote2.py
song_writer = "Willie"
message =  (f"{song_writer} wrote and recorded 'How could I leave if I never came here?'")
print(message)

#2-7 stripping names
name = "\t  Sandy Quinn    \n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

# 2-8 file_extensions
filename = "python_notes.txt"
print(filename)
print(filename.removesuffix(".txt"))

# 2-9 number_eight.py
print(6 + 2)
print(64 / 8)
print(15 - 7)
print(2 * 4)

# 2-10 favorite_number.py
favorite_number = (10 - 6)
message = f"my favorite number is , {favorite_number}!"
print(message)

# 2-11 comments
# I am doing these exercises tp learn Python
# 2-12 Zev_of_Python
import this
