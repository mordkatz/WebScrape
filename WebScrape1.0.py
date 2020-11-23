# Intro to Web Scraping with Python and Beautiful Soup by the Data Science Dojo

# To install beautiful soup open the command line and type pip install bs4

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

page_url = "http://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=GTX&bop=And&Page=1&PageSize=36&order=BESTMATCH"

# Openst up the connection grab the web page and download it
uClient = uReq(page_url)

# Read the web page
page_htm = uClient.read()

# Close the connection
uClient.close()

# Does the html parsing
page_soup = soup(page_htm, "html.parser")

# Gets the containers for all the graphics cards
containers = page_soup.findAll("div", {"class": "item-container"})

# Print how many container there are
print(len(containers))

# Loop through all the containers
for container in containers:
	# Get the brand of the graphics card
	brand = container.div.div.a.img["title"]
	print(brand)
	# Get the name
	image = container.a.img["src"]
	print(image)