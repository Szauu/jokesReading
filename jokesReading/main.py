import requests
import json
import os.path
import pyttsx3

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)
print(response.status_code)
jsonData = json.loads(response.text)
jokes = [jsonData]
print(jokes)


class Joke:

    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"Question: {self.setup}\npunchline: {self.punchline}!\n"

jokeList = []
filename = "jokes.txt"

for j in jokes:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokeList.append(joke)
    if os.path.isfile(filename):
        with (open(filename, "a")) as file:
            file.write(Joke.__str__(joke)+"\n")
    pyttsx3.speak(Joke.__str__(joke))



