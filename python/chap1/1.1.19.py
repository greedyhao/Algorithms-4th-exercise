def Fibonacci(N):
    current = 0
    after = 1
    for cnt in range(0,N):
        current,after = after,(after+current)
    return current

if __name__ == "__main__":
    for N in range(0,101):
        print(str(N) +' '+ str(Fibonacci(N)))
