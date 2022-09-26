import csv

with open('names.csv','r') as cvs_file:
    csv_reader = csv.DictReader(cvs_file)

    with open('new_names.csv','w') as new_file:
        fieldnames = ['first_name','second_name']

        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter='\t')
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer(line)
    

