first = 'Hello'
second = 'hello'

def compare(first, second):
    if first.upper() == second.upper():
        return True
    else: 
        return False
result = (compare(first, second))
print(result)