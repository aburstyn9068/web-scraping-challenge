# web-scraping-challenge
This repository contains the code files for a Mars web scraping project. The code scrapes several webistes for news articles, information, and images of Mars.

The initial web scrapping was completed using a Jupyter Notebook and the Python Pandas, BeatifulSoup, and Requests/Splinter libraries.

The first part of the project was to scrape the NASA Mars News website (https://redplanetscience.com/) and collect the latest news title and paragraph text from the page. This information was stored as a variable for later use.

The second part of the project was to scrape the JPL Mars Space Images website (https://spaceimages-mars.com) and collect the url information for the current featrued Mars image. The url was saved as a variable for later use.

The next part of the project was to scrape the Mars Facts website (https://galaxyfacts-mars.com) and collect the information in the table containing facts about Mars. The table data was saved using Pandas to later be used in the html file.

The final part of the scraping portion of the project was to Mars Hemispheres site (https://marshemispheres.com/) and obtain the url and title for each of the hemisphere images. The information collected was saved a variable for later use.

The jupyter notebook was converted to a .py file that converts the saved information into a dictionary and  uploads it to a MongoDB database.

A flask server is used to access the information stored in the MongoDB database and display it on a website. The html code includes an interactive button that is displayed on the website labeled "Scrape New Data." Clicking the button will run the python code to scrape new information and update the display.

Python and HTML code files and images of the website are included in this repository.
