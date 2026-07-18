movies = [
    {"title": "Inception", "year": 2010, "rating": 8.8},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0},
    {"title": "Interstellar", "year": 2014, "rating": 8.6},
    {"title": "Parasite", "year": 2019, "rating": 8.5},
    {"title": "The Godfather", "year": 1972, "rating": 9.2},
]

movie_ratings = [m["rating"] for m in movies]


def print_movies(movie):
    print(
        f"Title: {movie['title']} | "
        f"Year: {movie['year']} | "
        f"Rating: {movie['rating']}"
    )


# Print all movies rated above 8.7
print("--- Movies rated 8.7 and above ---")
for movie in movies:
    if movie["rating"] >= 8.7:
        print_movies(movie)


# Print movies sorted by rating descending
print("\n--- Movies sorted by rating in DESC order ---")

sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)

for mve in sorted_movies:
    print_movies(mve)


# Print the title of the highest rated movie
print("\n--- Highest rated movie ---")
highest_rated_movie = max(movies, key=lambda m: m["rating"])
print_movies(highest_rated_movie)


# Print the average rating
print(f"\nThe average movie rating is {sum(movie_ratings) / len(movie_ratings)}")
