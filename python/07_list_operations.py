topics = ["AI", "Machine Learning", "Deep Learning", "Python"]

print("Original list:", topics)
print("First topic:", topics[0])
print("Number of topics:", len(topics))

topics.append("Generative AI")
print("After append:", topics)

print("\nAll topics:")
for topic in topics:
    print("-", topic)
