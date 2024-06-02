def gen_secs():
    # Generate a generator that yields the number of seconds in a minute
    # and then the number of seconds in an hour
    
    return (sec for sec in range (0, 60))

def gen_minutes():
    # Generate a generator that yields the number of minutes in an hour
    # and then the number of minutes in a day
    
    return (min for min in range (0, 60))

def gen_hours():
    # Generate a generator that yields the number of hours in a day
    
    return (hour for hour in range (0, 24))

def gen_days(month, leap_year=True):
    # Generate a generator that yields the number of days in a month
    # and then the number of days in a year
    
    if month == 2:
        if leap_year:
            return (day for day in range (1, 30))
        else:
            return (day for day in range (1, 29))
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return (day for day in range (1, 32))
    else:
        return (day for day in range (1, 31))
    
def gen_months():
    # Generate a generator that yields the number of months in a year
    
    return (month for month in range (1, 12))

def gen_years(start=2019):
    # Generate a generator that yields the number of seconds in a year
    
    year = 0
    while True:
        yield start + year
        year += 1
        
def gen_time():
    # Generate a generator that yields the number of seconds in a minute
    # and then the number of seconds in an hour
    # and then the number of minutes in an hour
    # and then the number of minutes in a day
    # and then the number of hours in a day
    
    return ((hour, min, sec) for hour in gen_hours() for min in gen_minutes() for sec in gen_secs())

def gen_date():
    # Generate a generator that yields the number of days in a month
    # and then the number of days in a year
    # and then the number of months in a year
    # and then the number of seconds in a year
    
    return ((day, month, year, time) for year in gen_years() for month in gen_months() for day in gen_days(month) for time in gen_time())

def main():
    #for gd in gen_date():
    #    print("%02d/%02d/%04d %02d:%02d:%02d" % (gd[0], gd[1], gd[2], gd[3][0], gd[3][1], gd[3][2]))  

    counter = 0
    for gd in gen_date():
        if counter == 1000000:  
            print("%02d/%02d/%04d %02d:%02d:%02d" % (gd[0], gd[1], gd[2], gd[3][0], gd[3][1], gd[3][2]))  
        counter += 1

    # 12/01/2019 13:46:40
    #
if __name__ == "__main__":
    main()