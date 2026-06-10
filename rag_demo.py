documents = [
    "Snowflake is a cloud data warehouse",
    "dbt is used for data transformations",
    "Power BI is used for reporting"
]

question = input("Ask a question: ")

for document in documents:

    if question.lower().split()[0] in document.lower():

        print("\nRetrieved Document:")
        print(document)

        print("\nGenerated Answer:")
        print(document)

        break

else:

    print("No relevant document found")