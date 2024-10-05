def fibonacci(n):
    Fibo = [0, 1]  
    for i in range(2, n):
        next_val = Fibo[-1] + Fibo[-2] 
        Fibo.append(next_val)
    return Fibo


print(fibonacci(5))  
