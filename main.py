import os
import requests
import json
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv(".env")
username = os.getenv("USER")
password = os.getenv("PASSWORD")
api_key = os.getenv("API_KEY")
hashtags = os.getenv("HASHTAGS")

res = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
res = res.json()

img_url = res["hdurl"]
img_data = requests.get(f"{img_url}").content
with open('nasapic.jpg', 'wb') as handler:
    handler.write(img_data)

title = res["title"]
explanation = res["explanation"]
copyright_ = res["copyright"]

cl = Client()
cl.login(username, password)

cl.photo_upload("./nasapic.jpg", f"{title}\n\n    {explanation}\n\n\n    Copyright: {copyright_}\n\n\n{hashtags}")