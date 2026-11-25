"""Модуль с декораторами для логирования выполнения функций."""

from functools import wraps

def log(filename=None):
    def decorator(func):
        def write_log(message):
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(message + "\n")
            else:
                print(message)
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                message = (f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}")
                write_log(message)
                raise
            write_log(f"{func.__name__} ok")
            return result
        return wrapper
    return decorator