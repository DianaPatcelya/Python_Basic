def gen_geometric_progression(start, step):
    while True:
        yield start
        start *= step


start = -2
step = -5
progression = gen_geometric_progression(start, step)

for item in range(10):
    print(next(progression))
