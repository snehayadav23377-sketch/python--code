numbers = [10, 20, 30, 40, 50]
print(numbers)


fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)


numbers[2] = 35
print(numbers)


numbers = [10, 20, 30, 40, 50]
print(numbers[0])  # Output: 10


name ="sneha"
print(name) # Output: 's'


text = "python"
print(text[0])  # Output: 'p'


text = "python"
print(text[1:4])  # Output: 'tho'

arr = list(map(int, input().split()))
print(arr)

arr = [10, 20, 30, 40, 50]

for i in arr:
    print(i)


arr = list(map(int, input().split()))
arr.reverse()
print(arr)

arr = list(map(int, input().split()))

even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

s = input()
print(len(s))

s = input()
ch = input()

if ch in s:
    print("Present")
else:
    print("Not Present")
