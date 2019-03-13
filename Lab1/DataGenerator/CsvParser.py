import csv

with open('Populate.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('Cititation.csv', 'w') as new_file:
        fieldnames = ['title']
        csv_writer = csv.DictWriter(new_file, fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            del line['author'] #remove this column
            csv_writer.writerow(line)
            print(line)
#upload title to another csv
