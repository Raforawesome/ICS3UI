from urllib.request import urlopen, Request  # HTTP Utils
import json  # Decoding HTTP requests


hdr = {  # http request headers to ensure our request doesn't get denied
	'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0",
	'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
	# 'Accept-Encoding': "gzip, deflate",
	'Accept-Language': "en-CA,en-US;q=0.7,en;q=0.3"
}


def http.get(link):
	req = Request('https://www.raforaweso.me/ics/currencyrates/', headers=hdr)  # Create the request object
	response_raw = urlopen(req).read()  # Execute the request and read the return
	return response_raw