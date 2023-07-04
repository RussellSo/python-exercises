import doctest

def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """

    days = {
        "1": "Sunday", 
        "2": "Monday",
        "3": "Tuesday",
        "4": "Wednesday", 
        "5": "Thursday",
        "6": "Friday",
        "7": "Saturday"
        }

    # if day_of_week <1 or day_of_week >7:
    #     return None

    # return days[f"{day_of_week}"]

    return None if day_of_week <1 or day_of_week >7 else days[f"{day_of_week}"]

# weekday_name(15)
doctest.testmod(name='weekday_name', verbose=True)