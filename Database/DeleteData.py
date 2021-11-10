import csv

def deleteApp(appID):
    with open('Database/AppDB.csv', 'r') as out, open('Database/App.csv','w') as inp:
        csvwriter = csv.writer(inp)
        for row in csv.reader(out):
            if row[0] != appID:
                csvwriter.writerow(row)

