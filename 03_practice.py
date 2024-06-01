# reverse a string
str='Mrinmoy'
reverse_str=''
for char in str:
    reverse_str=char+reverse_str
print(reverse_str)

# find the first non-repeating character
name='teteer'
for i in name:
    if name.count(i)==1:
        print(i)
        break

# factorial
number=int(input("Enter a number: "))
factorial=1
for i in range(1,number+1):
    factorial=factorial*number
    number=number-1
print(factorial)

while number<0:
    factorial*=number
    number=number-1

print(factorial)

# Validate input
while True:
    n=int(input("Enter a number b/w 1 to 10:"))
    if 1<=n<=10:
        print("Thanks")
        break
    else:
        print("Invalid Number")