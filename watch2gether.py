import requests as rq
from bs4 import BeautifulSoup as bs
import random
from selenium import webdriver
import time
#Importing librarys

watch2gether_room = input('Your room number: ')
watch2gether = "https://www.watch2gether.com/rooms/" + watch2gether_room
# Gets the watch2gether room URL

url_search = input('Youtube search: ')
url_search = url_search.replace(' ', '+')
url = 'https://www.youtube.com/results?search_query=' + url_search + '&sp=EgIQAQ%253D%253D'
#Makes the search URL

session = rq.session()
yt_get = session.get(url)
soup = bs(yt_get.content, 'html.parser')
links = []
for yt_links in soup.find_all('a'):
	links.append(yt_links.get('href'))
#Get all the links and ands them to a list

result = [i for i in links if i.startswith('/watch')]
print(result)
#Makes a new list that only stores the links that start with "/watch"

vid_count = len(result)
print(vid_count)
#Displays how many video links were scraped

final_vid = random.randint(0, vid_count)
print(final_vid)
print(result[final_vid])
#Takes a random number between 0 and how many videos were scraped and displays the yt URL

"""

NOW COMES THE WATCH2GETHER SCRIPT

"""


options = webdriver.ChromeOptions()
options.add_argument('headless')
# prepare the option for the chrome driver


browser = webdriver.Chrome(options=options)
browser.get(watch2gether)
print(browser.current_url)
# Make the browser headless and opens the Watch2gether URL

time.sleep(5)
browser.save_screenshot('loltest.png')
search_button = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div[3]/i[1]')
search_button.click()
# finds the 'No Thanks' button and clicks it

search = browser.find_element_by_xpath('//*[@id="search-bar-input"]')
search.send_keys(result[final_vid])
# Enters the Youtube url in the search bar

search_click = browser.find_element_by_xpath('//*[@id="search-bar-form"]/div[2]/button')
search_click.click()
time.sleep(3)
video_enter = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div[2]/div/div[6]/div[1]/div/div[1]')
video_enter.click()
# Enters the URL into Watch2gether

time.sleep(1)
# Remove the comment symbol below if you want to save a screenshot before exit
# browser.save_screenshot('test.png')


print(browser.title)
print('\nDONE')
browser.quit()
# Quits the browser
