lst = [20,108, 30, 36, 24, 200, 50, 56,16]
n=lst[0]
for i in lst:
    if i > n:
        n = i
print(f"The largest number is: {n}")