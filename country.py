"""
Country names from the site http://example.webscraping.com
"""


from urllib.request import urlopen, Request

ACCU_URL = "http://example.webscraping.com/"

response = urlopen(ACCU_URL).read()
#response = response.decode('utf-8')
response = str(response)
#end = '</html>'
country_tag = 'png" />'

country_tag_size = len(country_tag)
country_tag_index = response.find(country_tag)
print("Index: ", country_tag_index)
country_value_start = country_tag_index + country_tag_size
print("Start: ", country_value_start)
country = ''

#I am working here to return the name of all countries
while country_tag_index != -1:
	for char in response[country_value_start:]:
		if char != '<':
			country += char
		else:
			country_tag_index = response.find(country_tag, country_value_start)
			country_value_start = country_tag_index + country_tag_size
			country += '\n'
			break
		
		
		


#print("Size: ", country_tag_size)
#print("Start: ", country_value_start)
#print("Index: ", country_tag_index)
#print("country_tag: ", country_tag)

print("Contry:\n", country)

