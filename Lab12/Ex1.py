#open a URL and print some content  from it. Print the instances of the <title> tag
import urllib.request
import ssl

ssl._create_default_https_context=ssl._create_unverified_context

url= "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"
encoding ='utf-8'

#open the web page
print((f"opening {url}..."))
webpage = urllib.reqest.urlopen(url)

#Iterate through each line in the webpage and search for <title>
for line in webpage:
    
