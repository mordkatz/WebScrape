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

# To put all the data that we get into a csv file that we can open up with excel
filename = "products.csv"
f = open(filename, "w")
# Make the headers for the csv file
headers = "brand, product_name, shipping\n"
f.write(headers)


# Loop through all the containers
for container in containers:
	 # Finds all link tags "a" from within the first div.
    make_rating_sp = container.div.select("a")

    # Grabs the title from the image title attribute
    # Then does proper casing using .title()
    brand = make_rating_sp[0].img["title"].title()

    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    product_name = container.div.select("a")[2].text

    # Grabs the product shipping information by searching
    # all lists with the class "price-ship".
    # Then cleans the text of white space with strip()
    # Cleans the strip of "Shipping $" if it exists to just get number
    shipping = container.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    price =  container.find("li", {"class": "price-current"})
    # prints the dataset to console
    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")
    print(price)
    # writes the dataset to file
    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")
f.close
