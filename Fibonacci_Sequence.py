
x = 0
y = 1

print("Fibonacci sequence:")
for i in range(10):
    print(x, end="  ")
    res = x + y
    x = y
    y = res