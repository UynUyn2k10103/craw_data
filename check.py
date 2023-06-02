import json

from vnpress_link import Output
import os
import csv
l = []
labels = ['thethao','suckhoe', 'kinhdoanh', 'giaoduc', 'giaitri']

for label in labels:
    l = []
    filename = f"link_{label}.json"
    with open(filename, 'r') as f: 
        l = json.load(f) 

    filename = f"finallink_{label}.csv"
    for so in range(len(l)):
        link = l[so]
        with(open('DenSo.txt', mode = 'w')) as file:
            file.write(str(so) + " " + label)
        try:
            Output(filename = filename, url = link, label = label)
        except:
            with open("bad_link.csv",  mode = 'a', newline = '', encoding = 'utf-8-sig') as badfile:
                headers = ['Link', 'Label']
                writer = csv.DictWriter(badfile, fieldnames = headers)
                if os.path.exists(filename) == False:
                    writer.writeheader()
                writer.writerow({headers[0] : link, headers[1] : label})

        
        

    




