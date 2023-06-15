import requests
from datetime import datetime
import time
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

current_appointment = datetime.strptime('2023-12-01', '%Y-%m-%d')

cookies = {
    '_ga': 'GA1.2.1136866613.1686784309',
    '_gid': 'GA1.2.1139931980.1686784309',
    '_gat': '1',
    '_yatri_session': 'ZDBTNnF2dnJqcTVNRVJqM3NjZnNRb0NjNm1QcHZOTU5heExESWdZTVUrMDJDWmlXckV1aVk1MnZlRGpSUTJOQkdkQXlFRFJVOHQ2bFlnT25Wa0tFZFhEczlsd1Y3Y21aR1Rlcm5ONEFVZGRBdm0wZFZId3IyUVZnR241WUtUeDhld3BuNytkeTN0bFFDYXBMRVZIK0s5WWwwU250UEJpdjVHYU1wczRYN1RVZG04Q3Z6N0loOUFrbWRCaUgxcEJ4RmZBblVSUzZYNm5MQUlKeDZHYVVqU2NLVXlUdlFpQ2k5cTdSYy9LTDhtaFNTUVlOa1JBUnpabTNJbmZ5WU5vTTZHWDNNZEhid25DcDl5Mk83TG1zell4Z1VGNy90VWZicnpDVmJYZjF2L0Y4T21DM2VQWk9EaE1SdkVpdmh0djQzVWlvZEJUR0RoblIvbHQ0RjBCL0YwQnBQaC95cktwc01hd3BzN3NVQnNOVFpKVS8zTUF3KzBqT0hneFpaSFJYMFppS3htdDh3NmJERytoUXJUNUNyNVVtemFSTlFRWHBvOVZFb0wyOWp1aVdmNmpZUXQ2ZXVBTWRmZjZ1S0pTK1FSN1dyN0lhN2FVLy9paFVXdTRCS2dJWU5lcXpJNjlwQStSTDJKTWR4bUNQbVhIekorRWRsY0JFTmUzRlc5RGtsQzhLcjJ0RlJKYVVBUThhR1d6K0pwNHVPOGZObDBieW11OUNWMWFYdC9jPS0tbWdHd1NuNzNORHk0UGY1QktHajJwQT09--3f6c7e8c00b0753df8a76004ad4c6e8b583723a7',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'ais.usvisa-info.com',
    'If-None-Match': 'W/"8376c608a41bf791cfc2c2bd5faf21ca"',
    'Referer': 'https://ais.usvisa-info.com/es-ar/niv/schedule/38923059/appointment',
    'sec-ch-ua': '"Google Chrome";v="108", "Chromium";v="108", ";Not A Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'X-CSRF-Token': 'XphOK5t5jys8mh8/XBfsmcDpljsrR4YdJVTQc94w4p5eJcdahzufdpJq3XkYD3o9OsURF+wjldcN1geIcj6GMw==',
    'X-Requested-With': 'XMLHttpRequest',
}

found = 'NOTHING FOUND'

while True:
    now = datetime.now().strftime('%H:%M:%S %d/%m')
    response = requests.get('https://ais.usvisa-info.com/es-ar/niv/schedule/49613228/appointment/days/28.json?appointments\\[expedite\\]=false', cookies=cookies, headers=headers)
    appointments = response.json()

    print('-text')
    print(response.text)
    print('-header')
    print(response.headers)

    top_five_appointments = appointments[:5]
    
    print(now+' | '+found+'\n-------------------------')

    for item in top_five_appointments:
        # Transform the date string into a datetime object
        datetime_obj = datetime.strptime(item['date'], '%Y-%m-%d')
        # Get a well formatted string of the datetime object
        datetime_str = datetime_obj.strftime('%d-%b-%Y')    
        if current_appointment > datetime_obj:
            print(f'{bcolors.BOLD}{bcolors.OKCYAN}{datetime_str}{bcolors.ENDC}')
            found = f'{bcolors.BOLD}{bcolors.FAIL}LAST FOUND AT {now}{bcolors.ENDC}'
            notification_url = 'https://cheddar-api.onrender.com/notification'  
            notification_body = {
                "message": "Fecha encontrada: "+datetime_str,
                "pwd": "NiceTry"
            }
            json_data = json.dumps(notification_body)
            notification_headers = {
                'Content-Type': 'application/json'
            }
            requests.post(notification_url, data=json_data, headers=notification_headers)
        else:
            print(f'{bcolors.ENDC}{datetime_str}')
    
    print('-------------------------\n')
    time.sleep(15)