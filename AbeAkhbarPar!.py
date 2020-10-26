import requests
import json
import pickle
from gtts import gTTS
import os


def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)


web = requests.get(
    "http://newsapi.org/v2/top-headlines?country=in&apiKey=8095e9a288d34117a60d29cbaf71222e")
data = web.text
# data2 = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=8095e9a288d34117a60d29cbaf71222e'
parsed = json.loads(data)
if __name__ == "__main__":
    # red = [[i] for i in range(0, 11)]
    # speak(parsed)
    for i in range(0, 11):
        # print(parsed['articles'][i]['title'])
        f = open("news.txt", "a")
        f.write(parsed['articles'][i]['title']+"\n\n")
        f.close()

        # print(type(parsed['articles'][i]['title']))
        # DataNews = parsed['articles'][i]['title']
        # f = open("news.txt", 'a')
        # Read.append(DataNews)
f = open("news.txt", "r")
x = f.read()
language = 'en'
audio = gTTS(text=x, lang=language, slow=False)
audio.save("newsapi.wav")
os.system("newsapi.wav")
