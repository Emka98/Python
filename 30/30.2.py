import functools

@functools.cache
def Fibonacci(rounds):
  if rounds in (1, 2): return 1
  return Fibonacci(rounds - 1) + Fibonacci(rounds - 2)

rounds = 33

print(f'Mass after {rounds} rounds :', Fibonacci(rounds))
