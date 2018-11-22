##############################
# Challenge 4
##############################

import urllib.request as req

n1 = "12345"
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + n1

response = req.urlopen(url)
html = response.read()
result = html.decode('utf8')
response.close()

print(result)