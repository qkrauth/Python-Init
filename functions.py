def hello():
    print("Hello Planet!")

hello()

def sum(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return # returns nothing/exiting the function
    return num1 + num2

total = sum(19, 9)
print(total)

def multi_items(*args):
    print(args)
    print(type(args))

multi_items("Q", "A", "K")

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(first = "Quinten", last = "Krauth")