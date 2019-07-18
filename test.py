def fib(num):
    print(num)
    if num == 8:
        raise Exception('fib(8)')
    if num in [0, 1]:
        return 1
    return fib(num-1) + fib(num-2)

if __name__ == "__main__":
    try:
        fib(20)
    except Exception as e:
        print(e)
