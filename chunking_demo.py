text = """
Snowflake is a cloud data warehouse.
dbt is used for data transformations.
Power BI is used for reporting.
Agentic AI uses tools and workflows.
"""

chunks = text.strip().split(".")

print("Chunks:\n")

for chunk in chunks:

    if chunk.strip():

        print(chunk.strip())