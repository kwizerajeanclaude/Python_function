def get_initial(name,force_uppercase=True):
    if force_uppercase:
        initial =name[0:1].upper()
    else:
        initial=name[0:1]
        return initial
first_name = input("Please enter your name")
first_name_initial = get_initial(first_name)
print("Your name is",first_name)
print("Initial is:",first_name_initial)
def multiply(a,b):
    return a * b
print(
    "The product of two number is:",
    multiply(
        int(input("Please enter first number")),
        int(input("Please enter ssecond number")),
        ),
)
