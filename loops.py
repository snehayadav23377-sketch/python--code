for i in range(5):
    print(i) 

    count = 1
    while count <= 5:
        print(count)
        count += 1


        n = int(input("Enter a number: "))
        for i in range(1, 11):
            print(n * i)



            for i in range(1, 6):
                if i == 3:
                    continue
                print(i)
                for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i) 

n = int(input())

sum = 0

for i in range(1, n + 1):
    sum += i

n = int(input())

fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)

n = int(input())

sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n //= 10

print(sum)

n = int(input())

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)

n = int(input())

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print(sum)
