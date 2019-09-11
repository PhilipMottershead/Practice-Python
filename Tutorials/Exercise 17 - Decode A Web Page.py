# Use the BeautifulSoup and requests Python packages
# print out a list of all the article titles on the New York Times homepage

# some requests code here for getting r_html
import requests

url = 'http://github.com'
r = requests.get(url)
print(r.text)