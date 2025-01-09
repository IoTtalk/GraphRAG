import requests
import os

dir = "ragtest/input"

os.makedirs(dir)

file = dir + "/book.txt"

if not os.path.exists(file) :
    url = "https://www.gutenberg.org/cache/epub/24022/pg24022.txt"
    response = requests.get(url, stream=True)
    data = response.text
    with open(file, "w", encoding="utf-8") as f:
        f.write(data)
