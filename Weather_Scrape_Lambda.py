import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime
import re

def scrapeWeather():

    try:

        url_list = 'https://www.hessenschau.de/wetter/messwerte/luftqualitaet-frankfurt-hoechst-bhf-100.html'

        res = requests.get(url_list)
        soup = BeautifulSoup(res.text, 'html.parser')
        #tabletext = soup.find_all(class_ = 'measurandTable__head js-pageableHead')[0].get_text().replace('\n', ' ')
        webtext = soup.find_all(class_ = 'measurandTable__lastRow js-column')[0].get_text().replace('\n', ' ').replace('ws', '0,0 WS')

        match_time = re.findall(r'[0-9]+[\:][0-9]+', webtext)
        wind_dir = re.findall(r'[A-Z]+', webtext)
        matches = re.findall(r'[0-9]+[\,][0-9]+', webtext)
        matches = [i.replace(',', '.') for i in matches]

        meas_time = match_time[0]
        current_date = datetime.today().strftime('%d.%m.%Y')

        date_and_time = current_date + ' ' + meas_time
        date_and_time_obj = datetime.strptime(date_and_time, '%d.%m.%Y %H:%M')

        return dict(Date_Time = str(date_and_time),
                                    T = float(matches[0]),
                                    WindSpeed = float(matches[1]),
                                    WindDir = str(wind_dir[0]),
                                    p = float(matches[2]),
                                    RH = float(matches[3]),
                                    O3 = float(matches[4]),
                                    PM10 = float(matches[5]),
                                    PM2_5 = float(matches[6]),
                                    NO2 = float(matches[7]),
                                    SO2 = float(matches[8]),
                                    Location = str('Frankfurt_Hoechst'))

    except Exception as err: print(err)
