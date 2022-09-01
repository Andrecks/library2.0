import requests
from datetime import datetime

def check_date(request):
    url = 'https://api.taxideli.ru/test/gettime'
    x = requests.post(url).json()['dataAns']/1000
    return{'date': datetime.utcfromtimestamp(x).strftime('%a, %d.%m.%Y %H:%M')}