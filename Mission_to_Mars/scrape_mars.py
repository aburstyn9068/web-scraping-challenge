# Import dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import requests

# Define scrape function
def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # Scrape the Mars News Site (https://redplanetscience.com/) and collect the latest 
    # News Title and Paragraph Text. Assign the text to variables that can be referenced later.


    # Target URL
    url = "https://redplanetscience.com/"


    # Connect to the website
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')



    # Get the latest news title
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_title



    # Get the paragraph text from the latest news article
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    news_p


    # Visit the url for the Featured Space Image site (https://spaceimages-mars.com).
    # Use splinter to navigate the site and find the image url for the current Featured Mars 
    # Image and assign the url string to a variable called "featured_image_url".


    # Target URL
    url = "https://spaceimages-mars.com"


    # Connect to the website
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')



    # Get featured image url
    featured_image_url = soup.find_all('a', class_='showimg fancybox-thumbs')[0]['href']
    featured_image_url = url + "/" + featured_image_url
    featured_image_url


    # Visit the Mars Facts webpage (https://galaxyfacts-mars.com) and use Pandas to scrape 
    # the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.


    # Target URL
    url = "https://galaxyfacts-mars.com"


    table = pd.read_html(url)[0]
    table = table[1:]
    table = table.rename(columns={0: "Mars - Earth Comparison", 1: "Mars", 2: "Earth"})
    table = table.set_index("Mars - Earth Comparison")
    table

    # Convert table to dictionary
    table_dict = table.to_dict()
    table_dict


    # Visit the astrogeology site (https://marshemispheres.com/) to obtain high resolution 
    # images for each of Mar's hemispheres.
    # Click each of the links to the hemispheres in order to find the image url to the full 
    # resolution image.
    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere 
    # title containing the hemisphere name. Use a Python dictionary to store the data using the keys
    # `img_url` and `title`.
    # Append the dictionary with the image url string and the hemisphere title to a list. 
    # This list will contain one dictionary for each hemisphere.


    # Target URL
    url = "https://marshemispheres.com/"
    # Connect to the website
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')


    # Find all image urls
    url_list = soup.find_all('a', class_='itemLink product-item')
    url_list



    # Extract the url
    page_urls = []

    for item in url_list:
        if (item["href"] != "#"):
            current_url = url + item["href"]
            if current_url not in page_urls:
                page_urls.append(current_url)
        
    page_urls


    # Save all image urls and hemisphere names
    hemisphere_image_urls = []

    for page in page_urls:
        browser.visit(page)
        html = browser.html
        soup = bs(html, 'html.parser')
        hemisphere_title = soup.find_all('h2', class_='title')[0].text.split()
        hemisphere_title.pop()
        hemisphere_title = " ".join(hemisphere_title)
        image_url = url + soup.find_all('img', class_='wide-image')[0]["src"]
        temp_dict = {"title": hemisphere_title, "img_url": image_url}
        hemisphere_image_urls.append(temp_dict)

    hemisphere_image_urls


    # Store scraped info in a dictionary
    mars_info = {
        "latest_news_title": news_title,
        "latest_news_paragraph": news_p,
        "featured_image": featured_image_url,
        "mars_facts": table_dict,
        "mars_hemispheres": hemisphere_image_urls
    }

    browser.quit()
    return mars_info
