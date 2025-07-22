from collections import Counter

# Count the frequency of words in a list
words = ['galaxy', 'nebula', 'asteroid', 'comet', 'gravitas', 'galaxy', 'stardust', 'quasar', 'galaxy', 'comet']
word_counts = Counter(words)

# Find the two most common words
most_common = word_counts.most_common(2)

# Output results
print(f"Word counts: {word_counts}")
print(f"Most common words: {most_common}")