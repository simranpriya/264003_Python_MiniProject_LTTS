def add_ten(x):
    if type(x) == str:
        number = int(x)
        result = number + 10
        return str(result)
    elif x is None:
        return None
    else:
        return x + 10

def subtract_ten(x):
    if type(x) == str:
        number = int(x)
        result = number - 10
        return str(result)
    elif x is None:
        return None
    else:
        return x - 10
