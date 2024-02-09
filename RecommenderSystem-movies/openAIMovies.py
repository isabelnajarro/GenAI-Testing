import openai
from openai import OpenAI
import re

class OpenAIMovies:
    def __init__(self, api_key, movie_dataset):
        self.api_key = api_key
        self.movie_dataset = movie_dataset

    def search_movies(self, criteria):
        matching_movies = []

        for movie in self.movie_dataset:
            match = True
            for key, value in criteria.items():
                if getattr(movie, key, None) != value:
                    match = False
                    break
            if match:
                matching_movies.append(movie)

        return matching_movies


    def generate_movie_prompt(self, user_input):
        prompt = f"I'm looking for {user_input}."
        return prompt

    def generate_movie_recommendation(self, user_input):
        client = OpenAI(api_key=self.api_key)
        prompt = self.generate_movie_prompt(user_input)
        print(prompt)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{prompt}"}
            ],    max_tokens=100 
            )
        print(response.choices[0].message.content.strip())
        return response.choices[0].message.content.strip()

    def recommend_movies(self, user_input):
        movie_recommendation = self.generate_movie_recommendation(user_input)
        print("OpenAI Recommendation:", movie_recommendation)
        criteria = {"overview": movie_recommendation}
        matching_movies = self.search_movies(criteria)
        if matching_movies:
            print("Matching Movies:")
            for movie in matching_movies:
                print(movie["title"])
        else:
            print("No matching movies found.")
