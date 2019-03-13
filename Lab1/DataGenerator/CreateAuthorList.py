import csv
def createAuthorList():
    my_list=[]
    current_index=0
    with open('Populate.csv', 'r') as csv_file: #get paper titles
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            del line['title'] #remove this column
            current_line=line['author']#take the current line
            if current_index == 0:
                my_list.insert(current_index, current_line)
                current_index = current_index + 1
            elif current_index > 0:
                if my_list[current_index - 1] != current_line:
                    my_list.insert(current_index, current_line)
                    current_index = current_index + 1
            else:
                print("ot")
    return my_list
print(createAuthorList())