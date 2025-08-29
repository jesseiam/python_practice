print("👋 Welcome To The Story Generator")

#Ask for user input
name = input("what is your name?: ")
age = int(input("how old are you?: "))
color = input("what is your fave color?: ")
hobby = input("what is your fave hobby?: ")
born = int(input("what year were you born?: "))

#calculations
age_5_years = age + 5
current_age = 2025 - born

#Output
print("---STORY TIME---")
print(f"Hi {name.upper()}, You're {age} years old")
print(f"Since you were born in {born}, you are {current_age} years old in 2025")
print(f"In 5 years, you'll be {age_5_years}")
print(f"Your favorite color is {color.lower()},and you love {hobby}")
print(f"So I guess we'll see you in 5 years, playing tennis while wearing {color} at age {age + 5}")
