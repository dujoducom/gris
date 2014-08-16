from bs4 import BeautifulSoup
import json
import requests

class gris(object):

	def __init__(self):
		print ">> init gris"

	def getSimilarImages(self, img_url):
		print ">> fetrching", img_url, "\n"

		d = self.__getDocument(img_url)

		print self.getImages(d)

	def __getDocument(self, img):
		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
		r = requests.get('https://www.google.com/searchbyimage?image_url='+img+'&q=', headers=headers, allow_redirects=True)
		r.encodoing = 'UTF-8'
		return r.text

	def getImages(self, doc):
		
		soup = BeautifulSoup(doc, from_encoding='UTF-8')
		bigImage = soup.find_all(id='imagebox_bigimages')
		a = bigImage[0].contents[0].contents[0].get('href')
		
		follow_link = "http://google.com" + a
		
		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
		r = requests.get(follow_link, headers=headers, allow_redirects=True)
		r.encodoing = 'UTF-8'

		soup = BeautifulSoup(r.text, from_encoding='UTF-8')	

		jso = soup.find_all(class_="rg_meta")
		
		
		d = "<b>nothing</b>"

		if len(jso) > 0:
			
			otp = '['

			for child in jso:
				# was .encode('utf8')
				otp = otp + child.string + ","

			otp = otp[0:-1] + ']'
			
			j = json.loads(otp)
		
			d = ""
		
			for child in j:
				d += child["tu"] + "\n"

		return d

def main():
	g = gris()
	g.getSimilarImages('https://31.media.tumblr.com/c8ff72cdb05fba30dc554d2f964ec739/tumblr_nabyljkXDx1qz6f9yo1_500.png')


if __name__ == '__main__':
	main()