# apply_decorator.py

def decorator_func(func):
    # A decorator function that prints a message before calling the original function
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    # Applies the decorator_func to the input function
    return decorator_func(func)
