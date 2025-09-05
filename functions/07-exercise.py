def clear_spaces_and_lower(text):
    text = text.replace(" ", "")
    return text.lower()


def reverse_text(text):
    letters = []
    for char in text:
        letters.insert(0, char.lower())
    return "".join(letters)


def is_palindrome(text):
    text = clear_spaces_and_lower(text)
    reversed_text = reverse_text(text)
    return text == reversed_text


print("This is a function to check if a text is a palindrome.")
print("Abba:", is_palindrome("Abba"))  # This will print True
print("Hello, World!:", is_palindrome("Hello, World!"))  # This will print False
print("Reconocer:", is_palindrome("Reconocer"))  # This will print True
print("AnONa:", is_palindrome("AnONa"))  # This will print True
print("Amo la paloma", is_palindrome("Amo la paloma"))  # This will print True
print("Esto no es un palíndromo:", is_palindrome(
    "Esto no es un palíndromo"))  # This will print False
