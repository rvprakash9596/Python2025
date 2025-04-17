def a():
    print("Hello Bhai")

# print(__name__) # It tells the name of the file name that is 'module'

if __name__ == "__main__":
    # if this code is executed by running the file its present in 
    print("We are directly running this code")
    a()
    print(__name__)