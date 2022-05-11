from datetime import date, datetime

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

# current_appointment = datetime.strptime('2022-09-15', '%Y-%m-%d')
current_appointment = datetime.strptime('2023-09-28', '%Y-%m-%d')

appointments = [
    {'date': '2023-09-27', 'business_day': True},
    {'date': '2023-09-28', 'business_day': True},
    {'date': '2023-10-05', 'business_day': True},
    {'date': '2023-10-10', 'business_day': True},
    {'date': '2023-10-11', 'business_day': True},
    {'date': '2023-10-12', 'business_day': True},
    {'date': '2023-10-13', 'business_day': True},
    {'date': '2023-10-17', 'business_day': True},
    {'date': '2023-10-18', 'business_day': True},
    {'date': '2023-10-19', 'business_day': True},
    {'date': '2023-10-23', 'business_day': True},
    {'date': '2023-10-24', 'business_day': True},
    {'date': '2023-10-25', 'business_day': True},
    {'date': '2023-10-26', 'business_day': True},
    {'date': '2023-10-27', 'business_day': True},
    {'date': '2023-10-30', 'business_day': True},
    {'date': '2023-10-31', 'business_day': True}
]

top_five_appointments = appointments[:5]

for item in top_five_appointments:
    # Transform the date string into a datetime object
    datetime_obj = datetime.strptime(item['date'], '%Y-%m-%d')
    # Get a well formatted string of the datetime object
    datetime_str = datetime_obj.strftime('%d-%b-%Y')    
    if current_appointment > datetime_obj:
        print(f'{bcolors.BOLD}{bcolors.OKCYAN}{datetime_str}')
    else:
        print(f'{bcolors.ENDC}{datetime_str}')
