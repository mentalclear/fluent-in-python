# From the archive, follow each link. find the image in the page, download the image

# Concepts
# 1. Donwloading stuff => urllib
# 2. Parse stuff out of HTML pages => BeautifulSoup

import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Download the index page
base_url = "https://apod.nasa.gov/apod/archivepix.html"
content = urllib.request.urlopen(base_url)
download_directory = "inetrmediate_python_prog/apod/imgs"

# For each link on the index page
for link in BeautifulSoup(content, "lxml").findAll("a"):
    print("Following the link:", link)
    href = urljoin(base_url,link["href"])

    # Follow the link and pull down the image from that linked page.
    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(href, img["src"])
        print("Downloading image: ", img_href  )
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
