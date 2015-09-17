from urllib2 import urlopen
from urlparse import urlparse
import re
from bs4 import BeautifulSoup

#1
address="https://www.realpython.com/practice/profiles.html"
html_page=urlopen(address) #grab data from profiles.html
html_text=html_page.read()
my_soup=BeautifulSoup(html_text)
hrefs=my_soup.find_all("a") # retrieving href 
#split url to remove the last part of url path
split_address=address.split("/")
split_address.pop(len(split_address)-1)
new_address= "/".join(split_address)

#retrieving links from tags to display the text on each page
for page_link in hrefs:
	Address=new_address+"/"+page_link["href"]
	text=urlopen(Address).read()
	My_soup=BeautifulSoup(text)
	print My_soup.getText()

	
	

	
