import csv

with open("HandlingCSV.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
    #for line in csv_reader:
     #   print(line)

    #next(csv_reader)   #  It escapes the frst line i.e., index Here, E-mail from csv file

    #for line in csv_reader:
    #    print(line[2])

    with open("new_names.csv","w") as new_file:
        #csv_writer = csv.writer(new_file, delimiter="-")  # since there is - in e-mail, it has double quote.😊😂

        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)

#..................................................................................................
#with open("new_names.csv","r") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter="\t")    # It reads file seperted in tabs.
#    for line in csv_reader:
#        print(line)
#..................................................................................................



