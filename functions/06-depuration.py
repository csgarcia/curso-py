def textLength(text):
    result = 0
    for _ in text:
        result += 1
    return result

print("This is a function to calculate the length of a text.")
length = textLength("Hello, World!")
print(length)  # This will print the length of the text, which is 13