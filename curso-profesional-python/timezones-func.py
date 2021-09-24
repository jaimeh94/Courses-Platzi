from datetime import datetime
import pytz

def get_date_time_from_timezone(city_name:str, timezone:str)-> str:
  city_timezone = pytz.timezone(timezone)
  city_time = datetime.now(city_timezone)
  print(f'{city_name}: {city_time.strftime("%d/%m/%Y, %H:%M:%S")}')


get_date_time_from_timezone("London", "Europe/London")
get_date_time_from_timezone("LA", "America/Los_Angeles")
get_date_time_from_timezone("CDMX", "America/Mexico_City")
get_date_time_from_timezone("Tokyo", "Asia/Tokyo")
get_date_time_from_timezone("Sydney", "Australia/Sydney")