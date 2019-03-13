import csv
from CreateAuthorList import createAuthorList
from CreatePaperList import createList
from RandomCit import randomNum
from RandomCit import randomIndex
myAuthor_list = createAuthorList()
size_Author= len(myAuthor_list)
print("------------")
print(size_Author)
myPaper_list=createList()
size_Paper=len(myPaper_list)



with open('Reviewers.csv', 'w') as new_file:
    row1={}
    fieldnames = ['author', 'reviewedPaper']
    csv_writer = csv.DictWriter(new_file, fieldnames)
    csv_writer.writeheader()
    print(size_Author)
    for i in range(size_Author-1):
        current_list = createList()
        for y in range(randomNum()):
            variable=randomIndex(current_list)
            element1=myAuthor_list[i]
            element2=current_list[variable]
            row1['author']=element1
            row1['reviewedPaper']=element2
            csv_writer.writerow(row1)
            current_list.remove(current_list[variable])






