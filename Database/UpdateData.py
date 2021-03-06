import csv

def updateSalary(accid:str,newSal:str):
    updateInfo = []
    with open('Database/Account/AccDB', 'r') as out:
        lines = out.readlines()
        for count, line in enumerate(lines):
            info = [x.strip() for x in line.split('|')][:-1]
            if str(info[-2]) == accid:
                lines[count] = ''
                for i in info:
                    lines[count] += i + ' | '
                lines[count] += f'{newSal}\n'
                info.append(newSal)
                updateInfo = info

    with open(f'Database/Account/AccDB', 'w') as inp:
        inp.writelines(lines)

    return updateInfo


def updateGeneralRecord(opt, data, recID):
    with open(f'Database/RecDir/{recID}.txt', 'r') as out:
        # try:
        lines = out.readlines()
        line = lines[opt].split(':')
        lines[opt] = f'{line[0]}: {data}\n'


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

    with open(f'Database/RecDir/{recID}.txt', 'w') as inp:
        inp.writelines(lines)

def updateAppointment(opt,data,appID):

    lastName = ''
    phoneNumber =''
    lines = list()

    with open('Database/App.csv', 'r') as out:
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

    with open('Database/App.csv', 'w') as inp:
        writer = csv.writer(inp)
        writer.writerows(lines)

    print(lastName, phoneNumber)
    return lastName, phoneNumber

def addPatient(recid,opt):

    with open(f'Database/DailyList', 'r') as out:
        # try:
        lines = out.readlines()
        line = lines[opt].strip()
        line = f'{line},{recid}\n'

        lines[opt] = line

    with open(f'Database/DailyList', 'w') as inp:
        inp.writelines(lines)

