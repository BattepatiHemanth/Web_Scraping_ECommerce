from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url='https://www.newegg.com/p/pl?d=laptops'

#calling web-page
client = uReq(url)

#downloading HTML
raw_html = client.read()

#Closing web-page
client.close()

#html parsing
page_soup = soup(raw_html, "html.parser")

 #collects all the results on the page

#to retrive info from page
 page_soup.anytag
 #(.findAll) will let us grab all the tags we specified
results = page_soup.findAll("div", {"class":"item-cell"})

#no. of results
len(results)

#to view at 1 result to find out which tags to use
results[0]

#taking only one result and putting it in a saperate variable as we can perform same actions on all rsults
result = results[0]

#creating CSV file
filename = "laptops.csv"
f = open(filename, "w")

headers = "brand, laptop_name\n"

f.write(headers)


#This will create a loop untill all the results are rad.
for result in results:
#by loking a tthe HTML we need to specify the hyriricy of the tags untill we get out desired information
#for tags we use .tag and tags inside tags we continue givign .tag untill we gt out information 
#for attributes inside a tag we will put the attributes inside a [""] after we specify the tag
	brand = result.div.div.a.img["title"]

#we are using the find class again to find a specific tag with the help of class because same tag has been repeated multiple times
	title_bin = result.findAll("a", {"class": "item-title"})
#this will take out the text from the a tag of the class.if there is a text present with no ags .text will extract it
	laptop_name = title_bin[0].text
#shipping details
	#shipping_des = result.findAll("a", {"class": "shipped-by-newegg"})
	#shiping = shipping_des[0].text

	print("brand: " + brand)
	print("laptop_name: " + laptop_name)
	#print("shiping: " + shiping)

	f.write(brand + "," + laptop_name.replace(","," ") + "\n")

f.close()






