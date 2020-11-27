# -------- DAY 3 "Conditions & Logical Operations" --------
# Goal: How to write conditions and logical operations
print('Welcome to iPython Stage < ^ _ ^ >')
age = int(input('How old are you?\n'))
if age > 0 and age <= 18:
    print(f"~~~~~~~~~~~~\nYour age is {age}\nSorry, you're not allow to enter.")
# We can simplify condition like this
elif 18 < age < 20:
    print(f'~~~~~~~~~~~~\nYour age is {age}\nAllowed to enter if there is somebody older with you.')
else:
    print(f'~~~~~~~~~~~~\nYour age is {age}\nAllowed to enter. Have fun!')
