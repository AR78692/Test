def my_decorator(func):
    def decorate():
        print("-------------")
        func()
        print("-------------")
    return decorate
def print_raw():
    print("Clear_text")
decorated_function=my_decorator(print_raw)
decorated_function()

#The brackets tell python that you are calling the function, 
#so when you put them there, it calls the function and assigns decorated_function 
#the value returned by my_decorator(print_raw) (which in this case is None).
