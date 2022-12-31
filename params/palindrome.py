def is_palindrome(value):
    value = value.replace(' ', '').lower()
    split = len(value) // 2

    if len(value) % 2 == 0:
        # even length
        left = value[:split]
        right = value[split:]

    else:
        # odd length
        left = value[:split]
        right = value[split+1:]
        
    return left == right[::-1]