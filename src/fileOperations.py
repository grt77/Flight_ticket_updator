import os
from dotenv import load_dotenv
load_dotenv()
import pandas as pd
from datetime import datetime

'''
it is used for the creating a file with data frame 
'''

def default_path_file_with_df(df,kind_of_file,date_of_file,type_of_folder,file_name,time):
   file_path=getFilePath(kind_of_file,date_of_file,type_of_folder,file_name,time)
   df.to_csv(file_path,index=False)

'''
Getting a file pointer , and it used for later pupose ,appending or writing to a file 

'''

def get_filepointer(kind_of_file,date_of_file,type_of_folder,file_name,time):
    file_path=getFilePath(kind_of_file,date_of_file,type_of_folder,file_name,time)
    fp=open(file_path,'a+')
    return fp

'''

creating a directories in a fashion of  foldername/year/month/day/filename

it will be easy for checking the ouputfiles even after certain amount of period, if it is in ths format  

'''


def getFilePath(kind_of_file,date_of_file,type_of_folder,file_name,time):
    folder_name = os.environ[type_of_folder]
    directory_path = os.path.join(folder_name, date_of_file[0:4], date_of_file[4:6], date_of_file[6:], kind_of_file)
    try:
        os.makedirs(directory_path)
    except FileExistsError:
        print("File already exits")
    file_path = os.path.join(folder_name, date_of_file[0:4], date_of_file[4:6], date_of_file[6:], kind_of_file,file_name+"_"+str(time) + ".csv")
    return file_path

'''

writing to a message to a file descriptor

'''

def write_file_withMessage(fp,message):
    try:
        fp.write("\n"+message)
    except Exception as e:
        print(e)

''''

closing a file descriptor 

'''


def close_file(fp):
    fp.close()