#1st Practical
def process_string(string, operation):
    result = ""
    for char in string:
        if operation == 'AND':
            result += chr(ord(char) & 127)
        elif operation == 'XOR':
            result += chr(ord(char) ^ 127)
    return result

input_string = "Hello, World!"
print("Input String:", input_string)

result = process_string(input_string, 'AND')
print("Result (AND):", result)

result = process_string(input_string, 'XOR')
print("Result (XOR):", result)
