import random

def generate_code(length=8):
    numbers = '0123456789ABCDEF'
    return ''.join(random.choice(numbers) for _ in range(length))

