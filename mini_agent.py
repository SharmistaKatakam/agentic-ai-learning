def calculator_tool(a, b):
    return a + b

question = input("Ask a question: ")

if "add" in question.lower():
    result = calculator_tool(100, 250)
    print("Agent selected: calculator_tool")
    print("Answer:", result)
else:
    print("I don't know which tool to use")