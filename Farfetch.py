import requests
import csv
import re
import json
import time

telegramUrl = "https://api.telegram.org/bot1237066723:AAFWTClE5CzpMtEuM-SXyyrOwQkEk87IYlc/sendMessage?chat_id=-424155986&text="

# Add URLS HERE
urls=["https://www.farfetch.com/hk/shopping/kids/teen-girl-clothing-7/items.aspx?view=90&designer=2857303",
      "https://www.farfetch.com/hk/shopping/kids/teen-boy-clothing-8/items.aspx?view=90&designer=2857303"];

l=[set()]*len(urls)

first=0
while(True):
    count=0
    new=set()
    for url in urls:
        urlset=set()
        response=requests.get(url=url);
        s=response.content.decode("utf-8")
        result = re.findall('<script>.+?</script>',s)
        for r in result:
            if("<script>window[\'__initialState_portal-slices-listing__\'] = " in r):
                s=r.replace("<script>window[\'__initialState_portal-slices-listing__\'] =","").replace("</script>","");
       
        y = json.loads(s)
        for product in y["listing"]["products"]:
            urlset.add(product["id"])
            if  product["id"] not in l[count] :
                new.add("ProductName: "+product["shortDescription"]+"   ImageUrl: "+product["images"]["cutOut"]+"   Url: "+urls[count])
        l[count]=urlset
        count=count+1
    print(len(new))
    if first==1 and len(new)!=0:
        requests.get(url=telegramUrl+"Total new Items In Stock: "+str(len(new)))
        for newP in new:
            requests.get(url=telegramUrl+newP)
    first=1
    time.sleep(15*60)
        
        