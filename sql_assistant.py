import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

question = input("Ask a SQL question: ")

prompt = f"""
You are an expert Snowflake SQL developer.

Convert the user's request into Snowflake SQL.

Return only SQL.

Question:
{question}
"""

response = model.generate_content(prompt)

print(response.text)