#steven 27/04/2020
import json
import datetime

def WriteFile(file,content):
    with open(file,'w',newline='\n') as f:
        f.write(content)

def getDataTime():
    daytime = datetime.datetime.now()
    today = datetime.date.today()
    
    daytime.__format__('%H:%M:%S')
    
    #t = str(today) + ' ' + str(daytime.hour) +':' + str(daytime.minute)
    t = str(today) + ' ' + str(daytime.__format__('%H:%M:%S'))
    print(t)
    return t

def updateJson(file='update.json'):
    updateJson = {"schemaVersion": 1, "label": "Last update", "message": "2020-04-27 08:07"}
    updateJson["message"] = getDataTime()
    print(json.dumps(updateJson))
    WriteFile(file,json.dumps(updateJson))
    
def main():
    updateJson()

if __name__=='__main__':
    main()
    