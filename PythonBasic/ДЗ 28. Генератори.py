def gen_geometric_progression(start, step):
    while True:
        yield start
        start *= step


start = -2
step = -5
progression1 = gen_geometric_progression(start, step)

for item in range(6):
    print(next(progression1))

print("-" * 50)

start = 10
step = 3
progression2 = gen_geometric_progression(start, step)

for item in range(6):
    print(next(progression2))
