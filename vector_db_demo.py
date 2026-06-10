vector_database = {}

text = "Snowflake"

embedding = []

for character in text:
    embedding.append(ord(character))

vector_database[text] = embedding

print("Vector Database:\n")

for key, value in vector_database.items():
    print(key, "->", value)