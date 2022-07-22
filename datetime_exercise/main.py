import datetime as dt

# Get today's date
current_date = dt.date.today()
print("Today's date is: " + str(current_date))

# Date
date1 = dt.date(2022, 1, 12)
print("Year: " + str(date1.year))
print("Month: " + str(date1.month))
print("Day: " + str(date1.day))

# Time
time1 = dt.time(11, 10, 12, 47823)
print("Time: " + str(time1))
print("Hour: " + str(time1.hour))
print("Minute: " + str(time1.minute))
print("Second: " + str(time1.second))
print("Microsecond: " + str(time1.microsecond))

# DateTime
datetime_obj = dt.datetime(2022, 11, 29, 23, 33, 20)
print("Datetime: " + str(datetime_obj))
print("Date: " + str(datetime_obj.date()))
print("Time: " + str(datetime_obj.time()))
print("Current Date & Time: " + str(dt.datetime.now()))

# TimeDelta
current_date_time = dt.datetime.now()
next_new_year = dt.datetime(2023, 1, 1, 0, 0, 0, 0)
remaining_time = next_new_year - current_date_time

print("Times left for next new year: " + str(remaining_time))

# Date String: strftime
string_date = current_date_time.strftime("%A, %B, %d, %Y")
print("Current DateTime: " + str(string_date))

# Date String: strptime
date_string = "21 June, 2022"
date_object = dt.datetime.strptime(date_string, "%d %B, %Y")
print("Date Object: " + str(date_object))
