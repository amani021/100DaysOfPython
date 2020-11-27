# -------- DAY 4 "Loops" --------
# Goal: Learn about loops (how to continue and stop) and catch the errors by (try/except)
print('Welcome to iPython Stage < ^ _ ^ >')
num = 1
while num <= 3:
    try:
        age = int(input('How old are you?\n'))
        if age <= 0:
            num += 1
            continue
        if age > 0 and age <= 18:
            print(f"~~~~~~~~~~~~\nYour age is {age}\nSorry, you're not allow to enter.")
            break
        # We can simplify condition like this
        elif 18 < age < 20:
            print(f'~~~~~~~~~~~~\nYour age is {age}\nAllowed to enter if there is somebody older with you.')
            break
        else:
            print(f'~~~~~~~~~~~~\nYour age is {age}\nAllowed to enter. Have fun!')
            break
    except:
        print('The value should be integer!')
        num += 1
print('ERROR: Entering the Correct Age!!')
