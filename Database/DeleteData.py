def deleteApp(appID):
    with open('Database/AppDB', 'r') as outline:
        lines = outline.readlines()

    with open('Database/AppDB', 'w') as outline:
        for line in lines:
            # if [x.strip() for x in line.split('|')][4] != appID:
             outline.write(line)
