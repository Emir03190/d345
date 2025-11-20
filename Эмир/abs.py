a = input()
s = len(a)
n = 0

for i in range(s):
    b = i + 1
    if a[i] == a[b]:
        n += 1
print(n) 