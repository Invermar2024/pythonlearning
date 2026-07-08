text = "python is easier when I practice python a little every day"

words = text.lower().split()
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
