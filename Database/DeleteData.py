import csv

def deleteApp(appID):

    lines = list()

    with open('Database/App.csv', 'r') as out:
        reader = csv.reader(out)
        for row in reader:
            if row[0] != appID:
                lines.append(row)

    with open('Database/App.csv','w') as inp:
        writer = csv.writer(inp)
        writer.writerows(lines)
