def fibonacci(n,m):
    fib1 = 0
    fib2 = 1
    fibonacci_list = []
    i = 0
    while i <= m:
        fib_next = fib1 + fib2
        fib1 = fib_next - fib1
        fib2 = fib_next
        if i >= n:
            fibonacci_list.append(fib1)
        i += 1
    return print("Ряд Фибоначчи с", n, "по", m,"\n", fibonacci_list)

fibonacci(0,10)
fibonacci(1,10)
fibonacci(2,10)