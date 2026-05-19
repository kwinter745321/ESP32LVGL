# test_fibonacci.py
# provided by google ai 18 may 2026

def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Print the first 10 terms
for num in fib_gen(10):
    print("{} ".format(num), end="")
print()
