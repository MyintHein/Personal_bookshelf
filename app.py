"""
-Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit:

-Add movies
-See movies
-Find a movie
-Stop running the program

Tasks:
[X]: Decide where to store movies
[X]: What is the format of a movie?
[X]: Show the user the main interface and get their input
[X]: Allow users to add movies
[X]: Show all their movies
[X]: Find a movie
[X]: Stop running the program when they type 'q'
"""

movies = []

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown keyword, Please try again.")

        user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    name = input('Movie name: ')
    director = input('Movie director: ')
    date = input('Release date: ')

    movies.append({
        'name' : name,
        'director' : director,
        'date' : date
    })

def show_movie(movies_list):
    for movie in movies_list:
        show_movie_details(movie)

def show_movie_details(movie):
    print(f"Name: {movie ['name']}")
    print(f"Director: {movie['director']}")
    print(f"date: {movie['date']}")

def find_movie():
    find_by = input("what properties? ")
    looking_for = input("searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movie(found_movies)


def find_by_attribute(items,expected, finder):
    found = []

    for i in movies:
        if finder(i) == expected:
            found.append(i)

    return found

menu()


print(movies)

