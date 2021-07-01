import logging
import urllib
from datetime import datetime
from urllib.request import urlopen
from sys import exit
from bs4 import BeautifulSoup as bs


def check_date_of_last_modification(date_to_check):
    url = "https://www.nalog.ru/opendata/7707329152-rsmp/"
    is_dates_equal = False

    try:
        # Download page and save to variable
        fp = urllib.request.urlopen(url)
        html_bytes = fp.read()

        html_str = html_bytes.decode("utf8")
        fp.close()

        # Find table and get interesting element
        soup = bs(html_str, 'lxml')
        # table = soup.find_all('table')

        # table_data = []

        # for elem in table:
        date_nalog = soup.find("td", text="Дата последнего внесения изменений").find_next_sibling("td").text
        # table_data.append(date)

        #print(date_nalog)
        nalog_date_fmt = '%d.%m.%Y'
        datetime_object_nalog = datetime.strptime(date_nalog, nalog_date_fmt)
        # 2020-11-10 00:00:00

        #datetime_object_check = datetime.strptime(date_to_check, nalog_date_fmt)
        #print(datetime_object_nalog)

        # только если месяц из поля «Дата последнего внесения изменений» равняется текущему
        is_dates_equal = datetime_object_nalog.date().month == date_to_check.month
    except Exception as e:
        logging.exception('Cant read table from site ')
        exit(2)

    return is_dates_equal


# # Debug
# if __name__ == '__main__':
#     today = date.today()
#
#     # date_time_str = '2020-11-10 23:15:27.243860'
#     # date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
#     # today = date_time_obj.date()
#
#     is_equal = check_date_of_last_modification(today)
#     print(is_equal)
