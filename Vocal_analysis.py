book1 = input("Enter text of Book 1:\n").lower()
book2 = input("\nEnter text of Book 2:\n").lower()

words1 = set(book1.split())
words2 = set(book2.split())

print("\nUnique words in Book 1:")
print(words1)

print("\nUnique words in Book 2:")
print(words2)

print("\nCommon words in both books:")
print(words1.intersection(words2))

print("\nWords unique to Book 1:")
print(words1.difference(words2))

print("\nWords unique to Book 2:")
print(words2.difference(words1))

print("\nTotal unique words across both books:")
print(words1.union(words2))

print("Number of unique words:", len(words1.union(words2)))