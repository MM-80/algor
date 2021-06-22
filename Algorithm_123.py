# Q #1
# Compute the sum of digits in all numbers from 1 to n. When a user enters
# a number n, find the sum of digits in all numbers from 1 to n.

n = int(input('Enter a number:'))
total = 0
while n > 0:
    digit = n % 10
    total = total+digit
    n = n//10
print("The total sum of digits is:", total)

----------------------------------------------------------------------------------------------------------------------------------------------------


# Q#2
# Find max number from 3 values, entered manually from a keyboard.

a = int(input('Enter first integer'))
b = int(input('Enter second integer'))
c = int(input('Enter third integer'))
print('Maximo is ', end='')
if b <= a >= c:
    print(a)
elif a <= b >= c:
    print(b)
elif a <= b >= b:
    print(c)


------------------------------------------------------------------------------


# Q#3
# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

number = int(input('Enter an integer number'))
remainder = number % 2
if remainder == 0:
    print(number, 'is an even Number')
else:
    print(number, 'is an odd Number')
