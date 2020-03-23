
#* Author : eXit-guy
#* API : https://corona-stats.online

import time
import requests
import json
import dateutil.parser

line_url = 'https://notify-api.line.me/api/notify'

line_token = 'P04wLqM52wwautYZY0oDdPDhY4rXkTck8NMRlDG8Ay6'

line_headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+line_token}

def getDataFromWeb():
    return json.loads(requests.get('https://corona-stats.online/Thailand?format=json').text)

def main():
    while(True):
        try :
            response = getDataFromWeb()
            report = 'Covid-19\nDev : eXit-Guy\nData : https://corona-stats.online\n\n'
            report += response[0]['country'] + '\n';
            report += 'confirmed : ' + str(response[0]['confirmed']) + '\n';
            report += 'recovered : ' + str(response[0]['recovered']) + '\n';
            report += 'deaths : ' + str(response[0]['deaths']) + '\n';
            report += 'lastUpdated : ' + str(dateutil.parser.parse(response[0]['lastUpdated']).strftime("%m/%d/%Y, %H:%M:%S %Z")) + '\n';
            print(report)
            r = requests.post(line_url, headers=line_headers , data = {'message':report})
            print(r.text)
        except:
            print('Something went wrong')
        time.sleep(5) # 5min
if __name__ == '__main__':
    main()
