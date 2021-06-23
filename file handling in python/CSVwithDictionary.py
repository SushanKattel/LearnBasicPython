import csv

with open("HandlingCSV.csv","r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    #for line in csv_reader:
        #print(line)
     #   print(line["E-Mail"])   #It prints only e-mail contaning feld.

    #   Now, we check for writing to the file 😂😂😂

    with open("new_namesCSV.csv","w") as new_file:
        fieldnames=["First_Name", "Last_Name", "E-Mail"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="\t")

        csv_writer.writeheader()  #This line writes the fieldnames at top. Otherwise, it would not have been written !! 😂😂😂😅

        for line in csv_reader:
            #del line["E-Mail"]   #This line deletes the e-mail fiels.

            csv_writer.writerow(line)
