from urllib2 import urlopen
import re
from bs4 import BeautifulSoup

 # grap html from page
html_text=urlopen("https://www.realpython.com/practice/dionysus.html").read()
names=["Name: ","Favorite Color: "]
for start_tag in names:
	start_index= html_text.find(start_tag)+len(start_tag) 
	end_index=html_text[start_index:].find("<")
	text=html_text[start_index:start_index+end_index].replace(" \n","")
	print text
	
	
for start_tag in ["Name: .*?[\n<]", "Favorite Color: .*?[\n<]"]:
    #match_result = re.search(start_tag, html_text)
    names = re.sub(".*: ", "", re.search(start_tag, html_text).group())
    print names.strip(" \n<")	

