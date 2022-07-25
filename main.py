camel = input("camelCase: ")


length = len(camel)
snakeCase = ""

for i in range(len(camel)):
    if camel[i].isupper():
        snakeCase = snakeCase + '_' + camel[i].lower()
    else:
        snakeCase += camel[i]

print("snake_case: ", snakeCase)
