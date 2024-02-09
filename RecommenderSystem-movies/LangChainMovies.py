import langchain

class LangChainProcessor:
    def __init__(self, movies_data):
        self.movies_data = movies_data
        self.langchainManager = langchain.LangChain()

    def process_user_input(self, user_input):
        result = self.langchainManager.match(user_input)
        criteria = {}
        if result:
            for key, value in result.items():
                criteria[key] = value
        return criteria

    def get_movies_by_criteria(self, criteria):
        filtered_movies = self.movies_data.copy()
        for key, value in criteria.items():
            if key == 'title':
                filtered_movies = filtered_movies[filtered_movies['title'].str.contains(value, case=False)]
            elif key == 'overview':
                filtered_movies = filtered_movies[filtered_movies['overview'].str.contains(value, case=False)]
            elif key == 'runtime':
                filtered_movies = filtered_movies[filtered_movies['runtime'] == value]
            elif key == 'adult':
                filtered_movies = filtered_movies[filtered_movies['adult'] == value]
            elif key == 'keywords':
                filtered_movies = filtered_movies[filtered_movies['keywords'].str.contains(value, case=False)]
            elif key == 'genres_associated':
                filtered_movies = filtered_movies[filtered_movies['genres_associated'].str.contains(value, case=False)]
            elif key == 'cast':
                filtered_movies = filtered_movies[filtered_movies['cast'].str.contains(value, case=False)]
            elif key == 'language_fav':
                filtered_movies = filtered_movies[filtered_movies['language_fav'].str.contains(value, case=False)]
            elif key == 'language':
                filtered_movies = filtered_movies[filtered_movies['language'].str.contains(value, case=False)]
        return filtered_movies
