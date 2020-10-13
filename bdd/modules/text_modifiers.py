
def uppercase(string):
    return string.upper()

def lowercase(string):
    return string.lower()

def only_numbers(string):
    available_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    string_numbers = ""
    for char in string:
        if char in available_numbers:
            string_numbers += char
    return string_numbers
