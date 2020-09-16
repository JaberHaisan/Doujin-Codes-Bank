# dj_bank.py - Store and use doujin codes.

import webbrowser

sites = {"nhentai": "https://nhentai.net/g/", "nexus": "https://hentainexus.com/view/",}
	
def links_saver(links, mode="a", text_file='Codes.txt'):
	"""Saves links in a text file."""
	with open(text_file, mode) as f_obj:
		for link in links:
			f_obj.write(link)
			f_obj.write('\n')

print("Enter 'q' to exit. Enter 'c' to start opening pages for stored codes"
+ " in your default browser.")
print("You can change the site for the code by entering their corresponding"
 + " keyword.\n")
print("Currently these keywords are available:")
print("\nKeyword -> Website")

for site, website in sites.items():
	# Removes https:// and suffix from printed website link.
	website = website[8:website.index("/", 8)]
	print(site, "->", website)
else:
	print()

links = []				
site = "nhentai"
while True:
	code = input("Code (%s)? " % site)
	if code == 'q' or code == "c":
		break
	if code == '':
		continue
	if code in sites:
		print("Website changed: %s -> %s" % (site, code))
		site = code
		continue
	links.append(sites[site] + code)

links_saver(links)

if code == "c":
	print("\nEnter the number of codes to be withdrawn.")
	
	with open("Codes.txt") as f_obj:
		links = f_obj.read().splitlines()
		
	unneccessary = ["\n", ""]
	links = [link for link in links if link not in unneccessary]	
			
	# Removing items from an iterating for loop causes items to be skipped
	# so a copy of links is made to avoid it.
	w_links = links[:]

	if not links:
		print("There are no codes stored currently.")
	else:      
		print("There are currently %s codes stored.\n" % (len(links)))
		
		while True:
			num = int(input("Number: "))
			# Rejects if num is not positive.
			if num < 0:
				print("Number has to be greater than or equal to 0")
				continue
			break
			       
		for i, link in enumerate(links[:num], 1):
			print("%s) Opening %s in browser." % (i, link))
			webbrowser.open(link)
			w_links.remove(link)
			links_saver(w_links, "w")	
		
		print("\nCompleted.")
