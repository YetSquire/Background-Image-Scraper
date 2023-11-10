# import requests
# from bs4 import BeautifulSoup
# URL = "https://www.google.com/search?sca_esv=559462882&rlz=1C1OPNX_enUS1066US1066&sxsrf=AB5stBhobQ9zy5GO1z1ObDBVFCWeHRIavg:1692813593593&q=art+gallery+pictures&tbm=isch&source=lnms&sa=X&ved=2ahUKEwiS1KqHrvOAAxUdkYkEHSrTBNoQ0pQJegQIDRAB&biw=1536&bih=707&dpr=1.25"
# getURL = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
# soup = BeautifulSoup(getURL.text, 'html.parser')
# images = soup.find_all('img')
# print(images)
# resolvedURLs = []
# for image in images:
#     src = image.get('src')
#     print(src)
#     width = image.get('width')
#     if (width != None and int(width) > 500): resolvedURLs.append(requests.compat.urljoin(URL, src))
# print(resolvedURLs)
# for image in resolvedURLs:
#     webs = requests.get(image)
#     open('picture.png', 'wb').write(webs.content)

from serpapi import GoogleSearch
import ctypes
import random
import requests
import os

params = {
  "q": "Desktop Backgrounds High Resolution",
  "engine": "google_images",
  "tbm": "isch",
  "num": "0",
  "ijn": "0",
  "api_key": "287924bc490784b3f9287311d77d0739df7af3c682ec4a5b6f8e119521551305"
}

search = GoogleSearch(params)
results = search.get_dict()
images = []
for image in results["images_results"]:
    if (image["original_width"] > 500): 
      images.append(image["original"])
x = int(random.random()*len(images))
webs = requests.get(images[x])
open('picture.png', 'wb').write(webs.content)
ctypes.windll.user32.SystemParametersInfoA(20, 0, os.path.abspath("picture.png").encode(), 0)

