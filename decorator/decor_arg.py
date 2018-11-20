def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_greeting(name):
    print(f"Great greeting, {name}")

if __name__ == '__main__'    :
    say_greeting('Peter')