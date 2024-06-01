# prime number checker
number=int(input("Enter a number:"))
is_prime=True
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            is_prime=False
            break
print(is_prime)

# Duplicate items
items=['apple','banana','mango','apple','lichi']
duplicate_item=set()
for item in items:
    if item in duplicate_item:
        print("Duplicate: ",item)
        break
    duplicate_item.add(item)