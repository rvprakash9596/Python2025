# WAP to ask the user to enter names of their 3 favorite movies & store them in a list

movies=[]
for i in range(1,4):
    movie=input(f"Enter movie name {i} :")
    movies.append(movie)
print(movies)

