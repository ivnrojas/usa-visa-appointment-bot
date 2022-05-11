import requests
from datetime import datetime
import time

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

current_appointment = datetime.strptime('2022-09-15', '%Y-%m-%d')

cookies = {
    '_ga': 'GA1.2.1697804321.1652268137',
    '_gid': 'GA1.2.1671280518.1652268137',
    '_yatri_session': 'K0U2VHhsZVNhSitnN3Rmd1lWWUpCSDZhMVZaRSthVHBma0E5cUVCa1VhRFhxOHhPR29UWWs0TnpCdVpPd3FvOFRBZSs5SHg2YWF2RkR4V2pmdWk5dXQyL1luTWxVRC82cVhNekFBVzZrcnB2cmszYXYvU1BXb2RZMjhnaEwvYkJiaTJabTJHUFNGdllMbWdsd21HYTdENzdFSHkzWHlKWjcyZmJRMG5OMzk2ZlVkSjV2dEJDa0hQdFpwbmNnYnB4NjdNelhTSGNFalhudjFMRGRiaDdLdjJtdGh5b2QzVzRxaTUxN3JwTzRmdTljVUhNRDlDc1JubExZZlE1dEpaMExMMnBKNURUK2R1eWRxSlpmRSs4L0hOck1BSDh1SGZyYVdDc3FndU9HNVN1UUVVM1ZiT1MrNVBYT1gxL2VOUXU5MHhEZ09ROGFKTC9BL1JMNlNFTjNWbHV0UTMxd1VreUZTWWozSUV2cUY1N215SnhuK1lMM2tnMDV6N2JabFMwNDFwWG9kQTBqb2U2MHoyeTQ1anBQQ0VnNjhoSEhxVm15T0lQUEtoVEUwWFVyTXFBK29kcXN4MzVZaDRmUy8vYnZhaXlETFRwbHhzQ05ENHMyM3oxTm5uZzdiUytpR1Jkd3VlN0dUNDZnRWVFQml2Ty8rTkNnOE00QW9pVnFnSTU5Z21DY3Z1VlBlREg2ZU9pK2g2OFdNK3ZxV2UvUDlXdThBdE5wOXhENEl3PS0tamk5T2JxNTJscElDU3hWWXBxbjhlZz09--813a2aa8e427067ce4cd49b0e861cd3f841469a0',
}

headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-CSRF-Token': 'eiDaUWITHb3PQ5EWnYmHwB86t5qvAt/3LhKBICtLb2MvNvb4Ph4ry2d1Mi5vL0dJMr/nCVUSyE2JM2wV4ca97A==',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-platform': '"Linux"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ais.usvisa-info.com/es-ar/niv/schedule/38923059/appointment',
    'Accept-Language': 'en-US,en;q=0.9,es-AR;q=0.8,es;q=0.7',
}

# response = requests.get('https://ais.usvisa-info.com/es-ar/niv/schedule/38923059/appointment/days/28.json?appointments\\[expedite\\]=false', cookies=cookies, headers=headers)
# print(response.json())

found = 'NOTHING FOUND'

while True:
    now = datetime.now().strftime('%H:%M:%S %d/%m')
    response = requests.get('https://ais.usvisa-info.com/es-ar/niv/schedule/38923059/appointment/days/28.json?appointments\\[expedite\\]=false', cookies=cookies, headers=headers)
    appointments = response.json()

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
        else:
            print(f'{bcolors.ENDC}{datetime_str}')
    
    print('-------------------------\n')
    time.sleep(10)