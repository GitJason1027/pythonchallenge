import requests
import re

def source(url):
	html = requests.get(url)
	html.encoding='utf-8'
	return html.text

def getnumber(html):
	number = re.findall('\d+',html,re.S)
	return number
def changeurl(num,url):
	target = re.sub('nothing=(\d+)','nothing=%d'%num,url,re.S)
	return target

if __name__ == '__main__':
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579'
	num = 0
	counter = 0
	while True:
		html = source(url)
		numlist = getnumber(html)
		if len(numlist)==1:
			num = int(getnumber(html)[0])
		else:break
		url = changeurl(num,url)
		counter = counter + 1
		print(counter)
		print(changeurl(num,url))
	print('Finish')
	
	#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
	#peak.html
