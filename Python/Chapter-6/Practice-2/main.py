#위에서 아래로

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

numbers = sorted(numbers, reverse = True)

for n in numbers:
    print(f"{n}", end = " ")