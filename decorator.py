# def my_decorator(func):
#     def wrapper():
#         print("Что-то происходит перед вызовом функции.")
#         func()
#         print("Что-то происходит после вызова функции.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Привет!")

# say_hello() 


# def myburger(func):
#     def wrapper():
#         print('*' *10)
#         func()
#         print('*' *10)
#     return wrapper

# @myburger
# def burger():
#     print('* burger *')
# burger()








# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def greet(name):
#     print(f"Привет, {name}!")

# greet("Alice")






