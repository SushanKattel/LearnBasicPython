import csv
import os
os.chdir("E:/program projects/Python projects/Advanced python/")
def Cancel():
    with open('game.csv', 'r') as inp:
        reader=csv.reader(inp)

        for row in reader:
            # print(row[1])
            if row[1] == "sudesh1":
                continue

            else:
                with open('game1.csv', 'a',newline='') as out:
                    write=csv.writer(out)
                    write.writerow(row)

        with open('game.csv', 'w') as out:
            pass

        with open('game1.csv', 'r') as inp:
             reader = csv.reader(inp)

             for row in reader:
                # print(row[1])

                with open('game.csv', 'a',newline='') as out:
                    write = csv.writer(out)
                    write.writerow(row)

        with open('game.csv', 'r') as inp:
            reader = csv.reader(inp)

            for row in reader:
                print(row[1])

    os.remove("game1.csv")