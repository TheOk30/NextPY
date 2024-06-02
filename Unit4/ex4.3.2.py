def f(x):
    yield x + 1
    print("test")
    yield x + 2
g = f(9)

# לא יודפס כלום למסך.