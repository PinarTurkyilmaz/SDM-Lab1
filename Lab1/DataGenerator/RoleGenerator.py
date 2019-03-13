import csv

with open('Populate.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('Role.csv', 'w') as new_file:
        row1 = {}
        fieldnames = ['title','author','roleofAuthor']
        csv_writer = csv.DictWriter(new_file, fieldnames)
        csv_writer.writeheader()
        previous_paper=''
        for line in csv_reader:
            if line['author']=='':
                continue
            else:
                current_paper=line['title']
                row1['title'] = line['title']
                row1['author']=line['author']
                if len(previous_paper)==0:
                    previous_paper=line['title']
                    roleOfAuthor='corresponding author'
                else:
                    if previous_paper==current_paper:
                        roleOfAuthor='normal author'
                    else:
                        previous_paper=current_paper
                        roleOfAuthor = 'corresponding author'
                row1['roleofAuthor']=roleOfAuthor
                csv_writer.writerow(row1)
                print(row1)

