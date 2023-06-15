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
ugly_appointment = datetime.strptime('2023-06-21', '%Y-%m-%d')

cookies = {
    '_ga': 'GA1.2.854241653.1686842990',
    '_gid': 'GA1.2.586893050.1686842990;',
    '_gat': '1',
    '_yatri_session': 'UjN1dDltVDRLcG15aHpUL0ZqRk9JaHRVYzFmS2IvNzlRb25XTHFVV2tlL0ZSeGoxeW9pNlNPVTNweGRtWGhZOFA1eEpRRDFDNkhNN1lQaVdGTktBSFVwSmFIUk9UOW9WOU03aWZNdnpVK1hGTjlPUXh2aU81aGVPS0U2cWxMamdHOHRFM3hYYUM4NWdLeDFOM2hlQjBBaVRPNXFORHppcDlaOW5mRXVuWUUxeTJ3RzFJcnlwQW5wRlh2bFVGVlhoNDVBaXZJdlRvQStySlQ3NEs3czBIZWwweEs5K1FxZkhwVG5GQ0xKYUdYZ0NkdUZGeWdlMm12VkswYTNoTU5nNkRSRnF5eHJTTGdwb3M3ZDdxMGJtMDlxRGdMb05kY2ZJZ3NHZUFqN1JDVERHcHgrQXp4VWdNVFVGOXEvN2xwZ1ZQNnozbjNPSXdUOVlocFNOVUxvNmhyQk0yZUFvNjQ4NFQ0eFhsSktZMm1Ta0ZLTlJOYWxmOGV4c1J4aGY3cUIvTVU0NXg5MG9PUU9wVXYyUUhZaTVHeFdxMGcyN0lBclVTV1ZoZ1FVdmNDQkYyK3A5aE9xSDNZMTRVZE5paWI1ZXh2allOQkp2K0dUVXp5V1E5OWxxNElDNlhUMi9TTDIxRlZ2R2o5RFJhd2JHSVhYZG1CKzdOeWRtYTl4UGpEV1E1TUFldnQ1b1Nqb2E0MXQxbFJ1V1JsaThjVS9VaDh4NU1GcWRtMW5YSDBZPS0tNmM5aXV1U0tpSUFOQ1JyMExVTUdYZz09--1bddb4f27a83dad80159411d21356c957161cbb0',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es',
    'Connection': 'keep-alive',
    'Host': 'ais.usvisa-info.com',
    'If-None-Match': 'W/"01e609dfbd6f5b9fe2541a1615852fb7"',
    'Referer': 'https://ais.usvisa-info.com/es-ar/niv/schedule/49613228/appointment',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-CSRF-Token': 'qCAKG2y7+/iXzxyqdiXOKiwRzyzn6j0DrfSi5jEeScJ4vz/BMsUWPrIKDwQiWRT36HfrExRURrS3Mvy37WhLbg==',
    'X-Requested-With': 'XMLHttpRequest',
}

found = 'NOTHING FOUND'

while True:
    now = datetime.now().strftime('%H:%M:%S %d/%m')
    response = requests.get('https://ais.usvisa-info.com/es-ar/niv/schedule/49613228/appointment/days/28.json?appointments\\[expedite\\]=false', cookies=cookies, headers=headers)
    print('-text')
    print(response.text)
    print('-header')
    print(response.headers)

    appointments = response.json()

    top_five_appointments = appointments[:5]
    
    print(now+' | '+found+'\n-------------------------')

    for item in top_five_appointments:
        # Transform the date string into a datetime object
        datetime_obj = datetime.strptime(item['date'], '%Y-%m-%d')
        # Get a well formatted string of the datetime object
        datetime_str = datetime_obj.strftime('%d-%b-%Y')    
        if current_appointment > datetime_obj and datetime_obj != ugly_appointment:
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