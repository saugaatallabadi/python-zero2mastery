# DECORATORS - Super boost your functions


from time import time


def my_decorator(func):  # func = hello()
    # def wrap_func(*args, **kwargs): # parameters are for hello() arguments
    def wrap_func(name_parameter):
        print('**********')
        # func(*args, **kwargs)
        func(name_parameter)
        print('**********')
    return wrap_func


@my_decorator
def hello(name):
    print(f'helllloooo {name}')


hello('saugaat')


# Example: Create @performance to see performance of your function


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()  # Current time
        result = fn(*args, **kwargs)
        t2 = time()  # Now what's the time
        print(f'took {t2-t1} ms')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5


long_time()


# Exercise

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}

print(user1['valid'])


def authenticated(fn):
    def wrapping(*args, **kwargs):
        if args[0]['valid']:  # [0] is for first argument which is 'user1'; there could've been other parameters too, but according to the Rule: params, *args, default parameters, **kwargs
            return fn(*args, **kwargs)
    return wrapping


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
