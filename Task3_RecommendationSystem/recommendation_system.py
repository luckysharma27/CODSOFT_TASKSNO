import csv


# Load movies from CSV
movies = []

with open("movies.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        movies.append(row)


def get_words(text):
    return set(text.lower().replace("|", " ").split())


def calculate_similarity(movie1, movie2):

    genre1 = get_words(movie1["genre"])
    genre2 = get_words(movie2["genre"])

    description1 = get_words(movie1["description"])
    description2 = get_words(movie2["description"])

    genre_score = len(genre1 & genre2)
    description_score = len(description1 & description2)

    return genre_score * 3 + description_score


def recommend_movies(movie_name):

    selected_movie = None

    for movie in movies:
        if movie["title"].lower() == movie_name.lower():
            selected_movie = movie
            break

    if selected_movie is None:
        print("\nMovie not found.")
        return

    recommendations = []

    for movie in movies:

        if movie["title"] == selected_movie["title"]:
            continue

        score = calculate_similarity(selected_movie, movie)

        recommendations.append((movie["title"], score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")
    print("-------------------")

    for i, (title, score) in enumerate(recommendations[:5], start=1):
        print(f"{i}. {title} (Similarity Score: {score})")


def show_movies():

    print("\nAvailable Movies:")
    print("-----------------")

    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie['title']}")


print("======================================")
print("      MOVIE RECOMMENDATION SYSTEM")
print("======================================")


while True:

    show_movies()

    print("\nEnter movie name to get recommendations.")
    print("Type 'exit' to close the program.")

    movie_name = input("\nEnter movie name: ")

    if movie_name.lower() == "exit":

        print("\nThank you for using the Movie Recommendation System!")
        break

    recommend_movies(movie_name)