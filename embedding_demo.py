text = "Snowflake is a cloud data warehouse"

embedding = []

for character in text:
    embedding.append(ord(character))

print("Text:")
print(text)

print("\nEmbedding:")
print(embedding)