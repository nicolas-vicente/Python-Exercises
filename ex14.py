from sys import argv

script, user_name, nickname = argv
# this variable will make it easier when asking for input (you don't have to keep typing it out; instead use the variable)
# used formatted string to include the script and user_name provided at the command line
prompt = f'{script} ({user_name})> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f'''
Hey, {user_name}...or {nickname} hehe.
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.      
''')