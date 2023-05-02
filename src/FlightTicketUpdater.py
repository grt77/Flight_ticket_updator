import os
import pandas as pd
import re
from dotenv import load_dotenv
from .DateOperations import get_date_object_unformatted,get_date_obj_formatted
from .fileOperations import default_path_file_with_df,get_filepointer,write_file_withMessage,close_file
from datetime import datetime
import sys

'''
Created a class with FlightTicketUpdater

constructor and trigger pipeline func:
   gonna load the data into pandas dataframe
   based on condition which mentioned in env variables (REG_EXP_DICT) , gonna execute on those columns 
   and there are some conditions tested 
   at last we are separating the succ and error records to a sep files 
'''



class FlightTicketUpdater:
    def __init__(self, filepath,date_arrived,debug=False):
        load_dotenv()
        self.filepath = filepath
        self.debug_log_file = debug
        self.date_arrived=date_arrived
        self.time_started=datetime.now().strftime("%H%M%S")


    def trigger_pipeline(self):
        self.log_file=get_filepointer(kind_of_file='',date_of_file = self.date_arrived,type_of_folder ='LOGS_FOLDER',file_name = 'logs',time=self.time_started)
        if self.debug_log_file:
            write_file_withMessage(self.log_file,"Pipeline is started :"+str(datetime.now()))
        self.data_df=pd.read_csv(self.filepath)
        check_valid_file=self.check_valid_schema_file()
        if not check_valid_file:
            write_file_withMessage(self.log_file, "please check the file with headers , they are invalid")
            sys.exit("File is invalid with headers")
        if self.debug_log_file:
            write_file_withMessage(self.log_file,"Done with loading to a file:"+str(datetime.now()))
        self.data_df=self.data_df.assign(Error='')
        reg_exp_checker_dict=eval(os.environ['REG_EXP_DICT'])
        for column in reg_exp_checker_dict:
            reg_exp=reg_exp_checker_dict[column]
            self.data_df=self.data_df.apply(self.regx_checker,args=(reg_exp,column,),axis=1)
        self.data_df = self.data_df.apply(self.ticketing_date_validation, axis=1)
        self.data_df = self.data_df.apply(self.book_cabin_validation, axis=1)
        self.error_df,self.succ_df=self.segregate_records()
        self.succ_df.columns=self.succ_df.columns.str.replace('Error', 'Discount_code')
        self.succ_df=self.succ_df.apply(self.apply_discount_code,axis=1)
        default_path_file_with_df(self.error_df,kind_of_file='error',date_of_file=self.date_arrived,type_of_folder='OUTPUT_FOLDER',file_name='error_records',time=self.time_started)
        default_path_file_with_df(self.succ_df, kind_of_file='success', date_of_file=self.date_arrived,type_of_folder='OUTPUT_FOLDER', file_name='success_records',time=self.time_started)
        close_file(self.log_file)


    '''
    
    it is used for the checking rex exp on paticular column , if doesn't satsified we are updating in error column in a dataframe
     
    '''
    def regx_checker(self,row,*args):
        reg_exp=args[0]
        column_checking=args[1]
        if self.debug_log_file:
            write_file_withMessage(self.log_file,"started reg exp executing "+reg_exp +"on "+column_checking+" "+str(datetime.now()))
        if re.match(reg_exp,str(row[column_checking])):
            pass
        else:
            row['Error']=row['Error']+column_checking+","
        return row

    '''
    it is used to check the ticket date is before  than travel date or not 
    
    '''


    def ticketing_date_validation(self,row):
        exception=0
        if self.debug_log_file:
            write_file_withMessage(self.log_file,"applying a ticketing validation "+str(datetime.now()))
        try:
            if os.environ['TRAVEL_DATE_FORMAT']=='%Y-%m-%d':
                travel_date_obj = get_date_obj_formatted(str(row['Travel_date']))
                ticket_date_obj = get_date_obj_formatted(str(row['Ticketing_date']))
            else:
                travel_date_obj = get_date_object_unformatted(str(row['Travel_date']))
                ticket_date_obj = get_date_object_unformatted(str(row['Ticketing_date']))
        except Exception as e:
            row['Error'] = row['Error'] + 'TravelDate,'
            exception=1
        if exception==0 and ((travel_date_obj=='None') or (ticket_date_obj=='None') or (ticket_date_obj>travel_date_obj)) :
            row['Error']=row['Error']+'TravelDate,'
        return row
    '''
    it used to check whether they opted out valid cabins or not , we storing the valid cabins in env  var [TYPES_BOOKED_CABINS]
    
    '''

    def book_cabin_validation(self,row):
        if self.debug_log_file:
            write_file_withMessage(self.log_file,"applying a book_cabin_validation "+str(datetime.now()))
        if row['Booked_cabin'] in os.environ['TYPES_BOOKED_CABINS'].split(","):
            pass
        else:
            row['Error']=row['Error']+'BookCabin,'
        return row

    '''
    it used for segregating the records for success and failures one 
    
    '''

    def segregate_records(self):
        error_records=self.data_df[self.data_df.Error!='']
        error_records=error_records.apply(self.modfiy_error_message,axis=1)
        success_records=self.data_df[self.data_df.Error=='']
        return error_records,success_records

    '''
    we are modifing the error message , removing a comma at end and adding a invalid string at end
    
    '''

    def modfiy_error_message(self,row):
        row['Error']=row['Error'][0:-1]+" Invalid"
        return row

    '''
    
    applying a discount codes for success records , these discount codes are storing in env variables DISCOUNT_CODES
    
    '''

    def apply_discount_code(self,row):
        offer_code_dict=eval(os.environ['DISCOUNT_CODES'])
        for fare_class in offer_code_dict:
            discount=offer_code_dict[fare_class]
            if re.match("^["+fare_class+"]{1}$",str(row['Fare_class'])):
                row['Discount_code']=discount
        return row


    '''
    
    checking the condition schema which we assumed , the schema of file are right or wrong 
    
    '''
    def check_valid_schema_file(self):
        file_columns=set(self.data_df.columns)
        schema_columns=set(eval(os.environ['VALID_SCHEMA_COLUMNS']))
        if len(schema_columns-file_columns)==0:
            return True
        else:
            return  False




