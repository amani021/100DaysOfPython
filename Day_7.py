# -------- DAY 7 "Fibonacci Sequence" --------
# Goal: Print the first 10 items of "Fibonacci Sequence"
# Eg: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)


print('Fibonacci Sequence:')
# Loop for print items
for i in range(10):
    if i == 9:
        print(fib(i))
    else:
        print(fib(i), end=', ')
