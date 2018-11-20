def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

def do_twice_ex(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_greeting(name):
    print(f"Great greeting, {name}")
    return f'{name}'

@do_twice_ex
def say_greeting_ex(name):
    print(f"Great greeting, {name}")
    return f'{name}'

if __name__ == '__main__'    :
    hi_peter = say_greeting('Peter')
    print(hi_peter)

    hi_coffee = say_greeting_ex('Coffee')
    print(hi_coffee)