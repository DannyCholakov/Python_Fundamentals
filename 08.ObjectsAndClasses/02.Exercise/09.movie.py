class Movie:
    __watched_movies = 0  # Class attribute to track watched movies

    def __init__(self, name: str, director: str):
        self.name = name
        self.director = director
        self.watched = False  # Default value for watched attribute

    def change_name(self, new_name: str):
        self.name = new_name

    def change_director(self, new_director: str):
        self.director = new_director

    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1  # Increase the class attribute for watched movies

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"
