import csv

with open('Reviewers.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('LastReview.csv', 'w') as new_file:
        row1 = {}
        fieldnames = ['author', 'reviewedPaper','content','status']
        csv_writer = csv.DictWriter(new_file, fieldnames)
        csv_writer.writeheader()
        previous_paper=''
        for line in csv_reader:
            row1['author'] = line['author']
            row1['reviewedPaper']=line['reviewedPaper']
            row1['content'] = 'The reviewer of the paper is : '+line['author']+'. The title of the paper is '+line['reviewedPaper']+' .'
            csv_writer.writerow(row1)







