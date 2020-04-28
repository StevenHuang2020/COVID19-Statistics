#steven 27/04/2020
import json
import datetime

def WriteFile(file,content):
    with open(file,'w',newline='\n') as f:
        f.write(content)

def getDataTime():
    daytime = datetime.datetime.now()
    today = datetime.date.today()
    
    #t = str(today) + ' ' + str(daytime.hour) +':' + str(daytime.minute)
    t = str(today) + ' ' + str(daytime.__format__('%H:%M:%S'))
    return t

def updateJson(file='update.json'):
    updateJson = {"schemaVersion": 1, "label": "Last update", "message": "2020-01-01 01:01"}
    updateJson["message"] = getDataTime()
    print(json.dumps(updateJson))
    WriteFile(file,json.dumps(updateJson))
    
def main():
    updateJson()

if __name__=='__main__':
    main()
    