def to_camel_case(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def camelize_dict(d):
    return {to_camel_case(k): v for k, v in d.items()}