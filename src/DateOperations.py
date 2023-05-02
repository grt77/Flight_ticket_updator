import re
from datetime import date
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
'''
Function is used for the getting the date object with - or / formatted 

2022/04/28 - identifies largest number as year(4 digits) , second largest as date(>12) and third largest as month
if nothing condition satisifies , returning a error message , we cant able to identify the date 
 

'''

def get_date_object_unformatted(datestring):
    error=''
    sep=''
    year, month, day = 0, 0, 0
    date_obj='None'
    if '/' in datestring:
        sep='/'
    elif '-' in datestring:
        sep='-'
    list_dateString_sep=[]
    splitted_date=datestring.split(sep)
    for i in splitted_date:
        list_dateString_sep.append(int(i))
    inp_year=max(list_dateString_sep)
    if re.match("[0-9]{4}",str(inp_year)):
        year=inp_year
        list_dateString_sep.remove(inp_year)
    inp_day=max(list_dateString_sep)
    if inp_day>12:
        day=inp_day
        list_dateString_sep.remove(inp_day)
        month=max(list_dateString_sep)
    try:
        if year and month and day:
            date_obj=date(year,month,day)
    except Exception as e:
        date_obj='None'
    return date_obj


'''
We storing the date format in env var, using that we creating a date obj 
-if not as formatted  , returning None

'''


def get_date_obj_formatted(dateString):
    try:
        date_obj=datetime.datetime.strptime(dateString,os.environ['TRAVEL_DATE_FORMAT']).date()
    except Exception as e:
        date_obj='None'
    return date_obj






