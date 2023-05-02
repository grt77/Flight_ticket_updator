#TICKET FLIGHT UPDATOR PROJECT

This is kind of a data pipeline , where we get customer data file in some time in a day , we need to do necessary transformations
and load into other location

##Getting started
```main.py is the callable python file , where other modules are present in the /src folder```


## .env File 
```We are storing the env variables in this file ```

##About Architecture 
```
After Job has run successful for the first time , u can able to see 
two new folders 

->  /output_date -> where output files will be produced 
      The folder structure inside the output folder is 
            year/month/day 
            eg: if we are processing file of day 2023-04-30
            The output folder structure can be seen as
                output_date/2023/04/30/error ->where invalid records present
                output_date/2023/04/30/success->where success records present
               


-> /logs_data-> where we can logs for the run of the paticular pipeline,
                The folder strcuture is same as the /output_data

U can see the images of output folder in /img folder 