'''✅ try Block:
It tries to take an input, converts it into an int, and prints it.
If everything goes well, it will hit the return and exit the function BUT…
❌ except Block:
If the input is invalid (like a string "abc"), it catches the exception (e.g., ValueError) and prints the error.
Then also hits the return to exit the function.
🔒 finally Block:
This block always executes, no matter what — even if a return was hit in try or except.
It’s used for cleanup actions (like closing a file, releasing resources, etc.).'''


# finally ka use hota  hai function me
def main():
    try:
        a=int(input("Hey,Enter a number :"))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey, I am inside of finally")

main()
