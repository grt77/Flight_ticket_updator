from datetime import datetime
from dotenv import load_dotenv
from src.FlightTicketUpdater import FlightTicketUpdater
import os
import pandas as pd

'''
Getting the file name and file formats from env variables passing these parms to FlightTicketUpdater class 

debug :True/False
    -This is used for debugging purpose , all the info related stored in los_data folder 
'''

load_dotenv()
file_date_format=os.environ['FILE_DATE_FORMAT']
file_format=os.environ['INPUT_FILE_FORMAT']
input_folder=os.environ['INPUT_FOLDER']
file_date_format=datetime.today().strftime(file_date_format)
file_name_to_process=os.path.join(input_folder,file_format+file_date_format+".csv")
flight_obj=FlightTicketUpdater(file_name_to_process,file_date_format,debug=True)
flight_obj.trigger_pipeline()

