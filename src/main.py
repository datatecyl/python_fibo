from module1.validate import valid_code
import module2.fibo as fibo


def print_fibonacci(nr):
    if valid_code(nr):
        print(fibo.fib(nr))


print_fibonacci(100)

print_fibonacci(0)
