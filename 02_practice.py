# print even number
number=10
for num in range(1,number+1):
    if num%2==0:
        print(num)


# multiplication table printer
num=int(input("Enter A Number: "))
for i in range(1,11):
    print(num,'X',i,'=',num*i)