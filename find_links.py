import requests
import re

#get url
url = input('Enter a URL (including `http://`): ')
#connect to the url
website = requests.get(url)
#read html as text 
html = website.text
#use re.findall to grab all the links
links = re.findall('"((http|ftp)s?://.*?)"', html) #creates a regular expression -> find all elements corresponding to that RE in html
#output links
for link in links:
    print(link[0])
