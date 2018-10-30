from bs4 import BeautifulSoup  #Beautiful soup library used to pull data from html ot xml
import urllib2               #To fetch source of the webpage ... just thinking .. xD

#Now fetching the source 
response = urllib2.urlopen("http://www.malacards.org/categories")
html = response.read()
soup = BeautifulSoup(html,'html.parser')

base = 'http://www.malacards.org'
diseases_list_link = []
dic = {}
for a in soup.findAll('a'):
	if 'diseases' in a.text:
		#goto diseases list under this category
		diseases_list_link.append(base + a.get('href'))
		
#now we have the link to to diseases from sub-category of them
leng = 0
for sub_disease in diseases_list_link:
	#goto first sub-category
	print sub_disease
	response1 = urllib2.urlopen(sub_disease)
	html1 = response1.read()
	soup1 = BeautifulSoup(html1,'html.parser')
	#now we are at diseases list page
	#html may have multiple tables so we store the list of those table
	tables = soup1.findChildren('table')
	#get the first table
	my_table = tables[0]
	rows = my_table.findChildren(['tr'])
	r = 1
	for row in rows:
		cnt = 0
		cells = row.findChildren('td')
		diseases_list_link = []
		inc = 0
		for cell in cells:
			cnt = cnt + 1
			if cnt == 1:
				c = cell.string
				c = int(c)
				if c == r:
					r = r+1
					inc = 1
			if cnt == 4 and inc == 1:
				value = cell.string
				#print value
				#value contains the name of the disease
				link = base + cell.a.get('href')
				#link contains the link to the desp of disease
				dic[value] = link
				leng = leng+1
	#print leng
#print dic
print leng

for dis in dic:
	print dis
	response2 = urllib2.urlopen(dic[dis])
	html2 = response2.read()
	soup2 = BeautifulSoup(html2,'html.parser')
	table = soup2.find('table',{'class':'borderless symptoms_table'})
	sympt = []
	if table != None:
		lists = table.findChildren('li')
		for li in lists:
			sympt.append(li.string)
			dic[dis] = sympt
	

				
				
				








