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

def updateMeasurement(pos, data, recID):
    with open(f'Database/RecDir/{recID}.txt', 'r') as out:
        # try:
        lines = out.readlines()
        line = lines[pos].split(':')
        lines[pos] = f'{line[0]}: {data}\n'
        print(lines)

    with open(f'Database/RecDir/{recID}.txt', 'w') as inp:
        inp.writelines(lines)

def updateAppointment(opt,data,appID):

    lastName = ''
    phoneNumber =''
    lines = list()

    with open('Database/AppDB.csv', 'r') as out:
        reader = csv.reader(out)
        for row in reader:
            if row[0] != appID:
                lines.append(row)
            else:
                row[opt] = data
                print(f'update: {row[opt]}')
                print(f'data: {data}')
                print(row)
                lines.append(row)
                lastName, phoneNumber = row[2],row[3]

    with open('Database/AppDB.csv', 'w') as inp:
        writer = csv.writer(inp)
        writer.writerows(lines)

    print(lastName, phoneNumber)
    return lastName, phoneNumber

