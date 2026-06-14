def squareroot(n):
    return n ** 0.5

print(f"user_defined_modules file: {__name__}")

#Just for understanding
# that value of __name__(Dunder variable) in user_defined_file is main
# but not in modules.py file so we can perform some task in this file as well
if __name__ == "__main__":
    print(squareroot(25))


