import pandas as pd

'''

This test case is used for only validate the book cabin , u may see all other columns are same for all test cases, but u can see diff in book cabin column 

'''

test_cases_for_book_cabin_validation=[(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Economy','Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Economy','Error':''},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'economy','Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'economy','Error':'BookCabin,'},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Premium','Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Premium','Error':'BookCabin,'},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'','Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'','Error':'BookCabin,'},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':123,'Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019-07-31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':123,'Error':'BookCabin,'},index=[0]).squeeze()
)
]

'''

it is used for only validating the travel date vs ticket date , u may see rest all other columns same 


'''



test_cases_for_ticketing_date_validation=[(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-30','Pax':1,'Ticketing_date':'2020-10-30','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Economy','Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-30','Pax':1,'Ticketing_date':'2020-10-30','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Economy','Error':'TravelDate,'},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2018-07-30','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'economy','Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2018-07-30','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'economy','Error':''},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':123,'Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Premium','Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':123,'Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Premium','Error':'TravelDate,'},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019/07/31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'','Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019/07/31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'','Error':'TravelDate,'},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'satish','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':123,'Error':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'satish','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':123,'Error':'TravelDate,'},index=[0]).squeeze()
)
]



'''

This test case used for only testing discount for a customer , except Fare class column , remaining column values u may see same for all test case 


'''
test_cases_for_applying_discount_validation=[(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-30','Pax':1,'Ticketing_date':'2020-10-30','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Economy','Discount_code':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'F','Travel_date':'2019-07-30','Pax':1,'Ticketing_date':'2020-10-30','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Economy','Discount_code':'OFFER_30'},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'X','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2018-07-30','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'economy','Discount_code':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'X','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2018-07-30','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'economy','Discount_code':''},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'AL','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':123,'Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Premium','Discount_code':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'AL','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':123,'Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'Premium','Discount_code':''},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':1,'Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019/07/31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'','Discount_code':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':1,'Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'2019/07/31','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':'','Discount_code':''},index=[0]).squeeze()
),
(
    pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'G','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'satish','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':123,'Discount_code':''},index=[0]).squeeze()
    ,pd.DataFrame({'First_name':'Teja','Last_name':'kumar','PNR':'ABC123','Fare_class':'G','Travel_date':'2019-07-31','Pax':1,'Ticketing_date':'satish','Email':'gattupall@gmail.com','Mobile_phone':9848517442,'Booked_cabin':123,'Discount_code':'OFFER_30'},index=[0]).squeeze()
)
]