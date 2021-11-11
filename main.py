import random
print("Choose heads or tails")


def coin():
    return random.choice([True, False])


print(coin())
