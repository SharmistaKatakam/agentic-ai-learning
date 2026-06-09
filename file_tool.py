def file_tool(file_name):
    with open(file_name, "r") as file:
        return file.read()

result = file_tool("employees.txt")

print(result)