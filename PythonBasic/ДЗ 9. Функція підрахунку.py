import random

random_list = [random.randint(0, 10) for i in range(200)]


def count_duplicates(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


summary_dictionary = {item: counts for item, counts in count_duplicates(random_list).items() if counts >= 0}

condition = lambda: "раз" if counts == 1 else ("рази" if counts == 2 or counts == 3 or counts == 4 else "разів")

for item, counts in sorted(summary_dictionary.items()):
    print(f"Число {item} зустрічається у первісному списку {counts} {condition()}")
