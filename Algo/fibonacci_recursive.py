def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  left = fibonacci(n-1)
  right = fibonacci(n-2)
  return left + right

print("fib(2)", fibonacci(2))
print("fib(3)", fibonacci(3))
print("fib(4)", fibonacci(4))
print("fib(5)", fibonacci(5))
