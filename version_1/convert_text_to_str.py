file_name = "script_1.txt"

file = open(file_name, "r+")
content = file.read()
# content = str(content)
content.replace("\n", "\\n")
file.write(content)

print(content)
file.close()