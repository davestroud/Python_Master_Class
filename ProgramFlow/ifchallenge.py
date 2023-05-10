name = input("Please enter your name: ")
age = int(input("How old are you? "))


# if 18 <= age < 31:
#     print("Welcome to club 18-30 holidays, {0}".format(name))
# else:
#     print("I'm sorry, our holidays are only for cool people")
  
# More Pythonic version with F strings
if age in range(18, 31):
    print(f"Welcome to the club 18-30 holidays, {name}")
else:
    print("I'm sorry, our holidays are only for cool people")