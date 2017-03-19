def encode(string):
    string = string.lower()
    current = ''
    result = ''
    for char in string:
        if char == ' ' or char == '.' or char == ',':
            continue
        if '0' <= char and char <= '9':
            current += char
            if len(current) == 5:
                result += current + ' '
                current = ''
            continue
        current += chr( ord('z') + ord('a') - ord(char))
        if len(current) == 5:
            result += current + ' '
            current = ''
    if current != '':
        result += current
    if result[-1] == ' ':
        result = result[:-1]
    return result

def decode(string):
    result = ''
    for char in string:
        if char == ' ':
            continue
        if '0' <= char and char <= '9':
            result += char
            continue
        result += chr(ord('a') + ord('z') - ord(char))
    return result
