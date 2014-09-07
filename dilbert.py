#!/usr/bin/python

## Import libraries

import requests
import re
from PIL import Image
from StringIO import StringIO
import io


## Set initial variables

dilbert_url = "http://www.dilbert.com/"
list_of_urls = []
image_number = 0
user_year = raw_input("Please enter the year you would like to acquire: ")

## Generate dates for user input year and add to list.

print "Generating dates..."

for month in range(1,13):
	for day in range(1,32):
		list_of_urls.append(dilbert_url + str(user_year) + "-" + str(month) + "-" + str(day))

print "Done generating dates"

## Get html, regex through it for image url and GET image file for each date.

print "Getting images..."

for line in list_of_urls:
	html_response = requests.get(line)
	temp_html_store = html_response.text
	try:
		urlSearch = re.compile('src="http(.*)strip.gif')
		findUrl = re.search(urlSearch, temp_html_store)
		temp_image_src = findUrl.group()
		temp_image_src = temp_image_src[5:]
		actual_url = requests.get(temp_image_src)
		image_number += 1
		temp_img_filename = str(image_number) + ".gif"
		with open(temp_img_filename, 'wb') as file:
			file.write(actual_url.content)
	except:
		pass

	
print "Done getting archive of images"