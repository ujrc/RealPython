from urllib2 import urlopen
import re
from bs4 import BeautifulSoup
import mechanize

my_browser=mechanize.Browser()
html_page=my_browser.open("https://www.realpython.com/practice/login.php")
my_browser.select_form("login")
my_browser["user"]="zeus"
my_browser["pwd"]="ThunderDude"

#using  wrond username and password
"""my_browser["user"]="Zeus"
my_browser["pwd"]="thunderDude"
"""
web_response=my_browser.submit()
html_text=html_page.get_data()
my_soup=BeautifulSoup(html_text)
print my_soup.title.string
for my_link in my_browser.links():
	my_browser.follow_link(my_link)
	print "Title:", my_browser.title()
	my_browser.back()
	print "Title:", my_browser.title()

print web_response.geturl()
print web_response.get_data()

