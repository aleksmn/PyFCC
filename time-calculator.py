'''
Write a function named add_time that takes in two required parameters and one optional parameter:

 a start time in the 12-hour clock format (ending in AM or PM)

 a duration time that indicates the number of hours and minutes
    (optional) a starting day of the week, case insensitive

Examples:

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM
 
add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday
 
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM
 
add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)
 
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)
 
add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)



'''



def add_time(start, duration, weekday = None):

    results = {}

    ampm = start.split(' ')[1].upper()

    start_h = int(start.split(' ')[0].split(':')[0])
    start_m = int(start.split(' ')[0].split(':')[1])

    if ':' in duration:
        dur_h = int(duration.split(':')[0])
        dur_m = int(duration.split(':')[1])
    else:
        dur_h, dur_m = int(duration), 0    

    reminder = (dur_h + (start_m + dur_m) // 60) % 12
    half_days = (dur_h + (start_m + dur_m) // 60) // 12

    #print(f'reminder: {reminder},  half_days: {half_days}')

    # Getting new AM/PM

    if (start_h + reminder >= 12) or ((start_h + reminder < 12) and half_days % 2 == 1):                    #and half_days == 0) or half_days % 2 == 1:
        if ampm == 'PM': new_ampm = 'AM'
        else: new_ampm = 'PM'
    else: new_ampm = ampm

    # Getting new Hours and Minutes

    if start_h + reminder == 12:
        new_h = 12
    else:
        new_h = (start_h + reminder) % 12

    new_m = str((start_m + dur_m) % 60).zfill(2)

    results['time'] = f'{new_h}:{new_m} {new_ampm}'
        
    # Getting Days Later (next day, 2 days later, 3 days later ...)

    days_later = half_days // 2

    if ampm == 'PM':
        days_later += half_days % 2
        if start_h + reminder >= 12:
            days_later += 1

    if days_later == 1:
        results['days_later'] = '(next day)'
    elif days_later > 1:    
        results['days_later'] =  f'({days_later} days later)'

    #print(f'days_later: {days_later}')


    # Getting Weekday
    
    if weekday:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday']
        weekday_index = weekdays.index(weekday.title())

        # new_weekday_index must be from 0 to 6

        new_weekday_index = (weekday_index + days_later) % 7
        results['weekday'] = weekdays[new_weekday_index]


    # Formatting output string

    result = f'{results["time"]}'

    if weekday:
        result += f', {results["weekday"]}'
    if days_later > 0:
        result += f' {results["days_later"]}'

    return result



print(add_time("8:16 PM", "466:02", "tuesday"))
# Returns: 6:18 AM, Monday (20 days later)

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM
 
print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday
 
print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM
 
print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)
 
print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)
 
print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)













