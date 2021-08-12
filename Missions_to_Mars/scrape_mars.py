from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    
    ## Make path for chrome driver exe and open
    driver_path = r'C:\Users\sceli\.wdm\drivers\chromedriver\win32\92.0.4515.107\chromedriver.exe'
    browser = Browser('chrome', executable_path = driver_path, headless = False)
    
    ## Visit the Mars news url
    url = "https://redplanetscience.com/"
    browser.visit(url)

    ## Pull html into beautiful soup parser
    html = browser.html
    soup = bs(html,'html.parser')
    
    ## Find the News Title and Paragraph Text. Assign the text to variables that you can reference later
    news_title = soup.find_all("div", class_="content_title")[0].get_text()
    news_p = soup.find_all("div", class_="article_teaser_body")[0].get_text()
    
    ## Visit the JPL Featured Image url
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    ## Pull html into beautiful soup parser
    html = browser.html
    soup = bs(html,'html.parser')

    ## Find the url of the featured image
    image = soup.find("img", class_="headerimage fade-in")['src']
    featured_image_url = url + image

    ## Visit the Mars Facts url
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)

    ## Pull html into beautiful soup parser
    html = browser.html
    soup = bs(html,'html.parser')

    ## Scrape the table containing facts about the planet including Diameter, Mass, etc.
    table = soup.find("table", class_="table table-striped").prettify()

    ## Visit the astrogeology url
    url = "https://marshemispheres.com/"
    browser.visit(url)

    ## Pull html into beautiful soup parser
    html = browser.html
    soup = bs(html,'html.parser')

    ## Get image urls
    hemisphere_image_urls = []
    hem_info = soup.find_all("div", class_="description")

    ## loop through hem_info entries to get img urls and names
    for hem in hem_info:
        ## get name of hemisphere
        hem_name = hem.find('h3').get_text()
        ## get href of hemisphere
        hem_url = hem.find('a', class_="itemLink product-item")['href']
        hem_image_url = url + hem_url
        ## navigate to image url and pull into beautiful soup
        browser.visit(hem_image_url)
        html = browser.html
        soup = bs(html,'html.parser')
        ## get image src
        img_src = soup.find('img', class_="wide-image")['src']
        ## create image link
        img_url = url + img_src
        ## now add into dictionary
        hem_dict = {
            'title' : hem_name,
            'img_url' : img_url
        }
        hemisphere_image_urls.append(hem_dict)
        
    ## Close browser
    browser.quit()

        
    ## Create dictionary with all necessary info from scrape
    mars_info_dict = {
        "news_title" : news_title,
        "news_p" : news_p,
        "featured_image_url" : featured_image_url,
        "facts_table" : table,
        "hemispheres" : hemisphere_image_urls
    }
    
    return mars_info_dict