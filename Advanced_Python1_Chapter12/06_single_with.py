# You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager


with (
open('file1.txt') as f1,
open('file2.txt') as f2
):
    content1 = f1.read()
    content2 = f2.read()

    print("Contents of file1.txt:")
    print(content1)

    print("\nContents of file2.txt:")
    print(content2)