is_male = False
is_tall = False
if is_male and is_tall:
    print("You're a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You aren't a male but are tall")
else:
    print("You're either not male and not tall ")