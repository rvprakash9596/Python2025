# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!


words={
    "Madad":"Help",
    "Kursi":"Chair",
    "Chay":"Tea",
    "Chawal":"Rice"
}

word= input("Enter the word which you want meaning of this word :")
print(f"The english meaning of {word} is:",words[word])


