import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name="h3")
movies.reverse()


for movie in movies:
    print(movie.text)
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(f"{movie.text}\n")
