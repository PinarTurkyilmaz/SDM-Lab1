import csv
from CreatePaperList import createList
from RandomCit import randomNum
from RandomCit import randomIndex
my_list = createList()
size= len(my_list)

print(my_list)


with open('Keywords.csv', 'w') as new_file:
    row1={}
    fieldnames = ['title', 'keyword']
    csv_writer = csv.DictWriter(new_file, fieldnames)
    csv_writer.writeheader()
    for i in range(size):
        current_list = ['data management','indexing', 'data modeling', 'big data', 'data processing', 'data storage','data querying','Software', 'Hardware', 'TCP/IP','security policy',
                'modeling', 'literature', 'security', 'biyology']
        for y in range(randomNum()):
            variable=randomIndex(current_list)
            element1=my_list[i]
            element2=current_list[variable]
            row1['title']=element1
            row1['keyword']=element2
            csv_writer.writerow(row1)

            current_list.remove(current_list[variable])






