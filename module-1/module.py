
# print("I like to be a module.")
print(__name__) # module


# ? Detecting the context in which your code has been activated
counter = 0 # It counts how many time the functions have been invoked
if __name__ == "__main__":
    print("I prefer to be a module.") # We are on main space
else:
    print("I like to be a module.") # We are on module space

    