nums = list(range(1, 5))
cube = list(map(lambda x: x**3, nums))
print(cube)

def sort_by_length(words):
    return sorted(words, key=lambda x: len(x))

words = ["alpha", "beta", "charlie", "delta", "echo"]
print(sort_by_length(words))
