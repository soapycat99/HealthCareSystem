import csv

def updateGeneralRecord(opt, data, recID):
    with open(f'Database/RecDir/{recID}.txt', 'r') as out:
        # try:
        lines = out.readlines()
        line = lines[opt].split(':')
        lines[opt] = f'{line[0]}: {data}\n'
        print(lines)

    with open(f'Database/RecDir/{recID}.txt', 'w') as inp:
        inp.writelines(lines)

    # except Exception as ex:
    #     template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    #     message = template.format(type(ex).__name__, ex.args)
    #     print(message)

def updateAppointment(opt,data,appID):

    lastName = ''
    phoneNumber =''

    with open('Database/AppDB.csv', 'r') as out, open('Database/App.csv', 'w') as inp:
        csvwriter = csv.writer(inp)
        for row in csv.reader(out):
            if row[0] != appID:
                csvwriter.writerow(row)
            else:
                row[opt] = data
                print(f'update: {row[opt]}')
                print(f'data: {data}')
                print(row)
                csvwriter.writerow(row)
                lastName, phoneNumber = row[2],row[3]
    print(lastName, phoneNumber)
    return lastName, phoneNumber

