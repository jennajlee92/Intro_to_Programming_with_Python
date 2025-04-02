from datetime import datetime

hour = datetime.now().hour

name = input("What's your name?\n")

if hour < 12:
    print(f"Good Morning, {name}!")
elif 12 <= hour < 18:
    print(f"Good Afternoon, {name}!")
else:
    print(f"Good Evening, {name}!")