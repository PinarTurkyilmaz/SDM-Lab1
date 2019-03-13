import csv
from CreateAuthorList import createAuthorList
from RandomAffiliation import randomNum
from RandomAffiliation import ranOrganization
myAuthor_list = createAuthorList()
size_Author= len(myAuthor_list)
print("------------")
print(size_Author)
university=['University of Amsterdam','Leiden University','Maastricht University','Delft University of Technology','University of Granada','International University of Andalusia'
            ,'University of Zaragoza','Polytechnic University of Catalonia','University of Barcelona', 'University of Santiago de Compostela','Heidelberg University', 'University of Munich','University of Marburg']
company=['Boeing','The Adecco Group','Nestle','Procter & Gamble','General Electric','Apple','McKeson','Compass Group','Accenture','Facebook','Google','Airbnb','Amazon']
print(len(university))
print(len(company))

with open('Affiliation.csv', 'w') as new_file:
    row1={}
    fieldnames = ['author', 'organizationType','organizationName']
    csv_writer = csv.DictWriter(new_file, fieldnames)
    csv_writer.writeheader()
    print(size_Author)
    for i in range(size_Author-1):
        value=randomNum()
        if value==1:
            element2='university'
            variable=ranOrganization()
            element3=university[variable]

        else:
            element2='company'
            variable=ranOrganization()
            element3=company[variable]

        element1 = myAuthor_list[i]
        row1['author'] = element1
        row1['organizationType'] = element2
        row1['organizationName'] = element3
        csv_writer.writerow(row1)
