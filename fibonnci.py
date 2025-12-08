n = int(input("Enter number: "))
a, b = 0, 1
sum = 0

for i in range(n):
    print(a, end=" ")
    sum += a
    a, b = b, a + b

print("\nSum:", sum)
