import random
# Split string method
# Teacher solution:

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Get the total number of items in list

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is buying the meal today!")

person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is buying the meal today!")