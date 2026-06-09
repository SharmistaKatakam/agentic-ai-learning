# Agentic AI Learning

This repository contains my learning exercises and mini-projects related to Agentic AI concepts.

## Topics Covered

- LLM Models (Google Gemini)
- Prompt Engineering
- Tool Calling
- Function Calling
- SQL Assistant (Text-to-SQL)
- File Tool
- Weather Tool
- Calculator Tool

## Projects

### 1. SQL Assistant
Converts natural language questions into SQL queries using Gemini.

Example:
User: Show top 10 customers by sales

Output:
SELECT customer_name,
       SUM(sales_amount)
FROM sales
GROUP BY customer_name
ORDER BY SUM(sales_amount) DESC
LIMIT 10;

### 2. Calculator Tool
Simple tool for performing calculations.

### 3. File Tool
Reads data from a text file.

### 4. Weather Tool
Returns weather information for a given city.

