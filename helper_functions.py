from datetime import date
import time

def get_date(inputString):
         inputString.strip()
	 try:
        	date_array = [int(val) for val in inputString.split(" ")]
	 except Exception as e:
		print(str(e))
         due_date = date(date_array[0], date_array[1], date_array[2])
         return due_date

