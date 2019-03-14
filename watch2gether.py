import requests as rq
from bs4 import BeautifulSoup as bs
import random
from selenium import webdriver
import time
import webbrowser
# importing librarys

try:
	file = open("room.txt", "r")
	with open('room.txt', 'r') as myfile:
		last_room = myfile.read()

except FileNotFoundError:
	print('Your room file were not found!')
# try to open room.txt and if it's not found just prints an error message


watch2gether_room = input('Do you want to load your last room? \n1. Yes\n2. No\n3. Create new room \nChoose between 1 and 3: ')
if watch2gether_room == str(1):
	watch2gether = "https://www.watch2gether.com/rooms/" + last_room
	print('Your room are: ' + watch2gether)
elif watch2gether_room == str(2):
	watch2gether_input = input('Your room: ')
	watch2gether = "https://www.watch2gether.com/rooms/" + watch2gether_input
	print('Your room are: ' + watch2gether)
elif watch2gether_room == str(3):
	new_room_options = webdriver.FirefoxOptions()
	new_room_options.headless = True
	new_room_options.muted = True
	# prepare the option for the chrome driver

	new_room = webdriver.Firefox(options=new_room_options)
	new_room.get('https://www.watch2gether.com/')
	# print(browser.current_url)
	# make the browser headless and opens the Watch2gether URL

	create_room = new_room.find_element_by_xpath('//*[@id="create_room_form"]')
	create_room.click()

	time.sleep(2)
	w2g_new_room = new_room.current_url
	watch2gether = new_room.current_url

	new_room.delete_all_cookies()
	new_room.close()
	new_room.quit()
	# quits the browser

	webbrowser.open(w2g_new_room)
else: 
	print('\nERROR... You need to choose between 1 and 3'*4)
	exit(0)




url_search = input('Youtube search: ')
url_search = url_search.replace(' ', '+')
url = 'https://www.youtube.com/results?search_query=' + url_search + '&sp=EgIQAQ%253D%253D'
# makes the search URL

session = rq.session()
yt_get = session.get(url)
soup = bs(yt_get.content, 'html.parser')
links = []
for yt_links in soup.find_all('a'):
	links.append(yt_links.get('href'))
# get all the links and ands them to a list

result = [i for i in links if i.startswith('/watch')]
# makes a new list that only stores the links that start with "/watch"

vid_count = len(result)
print('Found ' + str(vid_count) + ' videos')
# print(vid_count)
# displays how many video links were scraped

final_vid = random.randint(0, vid_count)
# print(final_vid)
# print(result[final_vid])
video = 'youtube.com' + result[final_vid]
# takes a random number between 0 and how many videos were scraped and displays the yt URL

"""

NOW COMES THE WATCH2GETHER SCRIPT

"""


options = webdriver.FirefoxOptions()
options.headless = True
options.muted = True
# prepare the option for the chrome driver


browser = webdriver.Firefox(options=options)
browser.get(watch2gether)
# print(browser.current_url)
# make the browser headless and opens the Watch2gether URL

time.sleep(3)
#browser.save_screenshot('debug0.png')
#search_button = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div[3]/i[1]')
#search_button.click()
# finds the 'No Thanks' button and clicks it

search = browser.find_element_by_xpath('//*[@id="search-bar-input"]')
search.send_keys(video)
# enters the Youtube url in the search bar

search_click = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div[1]/form/div[2]/button')
search_click.click()
time.sleep(3)
video_enter = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[4]/div[2]/div/div[6]/div[2]/div/div[1]')
video_enter.click()
# enters the URL into Watch2gether


# (DEBUG) Remove the comment symbol below if you want to save a screenshot before exit
# browser.save_screenshot('debug.png')


print(watch2gether_room)
if watch2gether_room == str(2):
	Save = open('room.txt', 'w')
	Save.write(watch2gether_input)
	Save.close()
	print('\nYour room was saved.')
else:
	pass

print('\nYour video is now posted to: ' + browser.current_url)
# prints a confirmation

browser.delete_all_cookies()
browser.close()
browser.quit()
# quits the browser