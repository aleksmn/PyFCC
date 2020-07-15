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

    print(f'reminder: {reminder},  half_days: {half_days}')

    if (start_h + reminder >= 12 and half_days == 0) or half_days % 2 == 1:
        if ampm == 'PM': ampm = 'AM'
        else: ampm = 'PM'

    new_h = (start_h + reminder) % 12
    new_m = str((start_m + dur_m) % 60).zfill(2)

    result = f'{new_h}:{new_m} {ampm}'

    

    # Getting Weekday
    
    if weekday:
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                    'Friday', 'Saturday', 'Sunday']
        weekday_index = weekdays.index(weekday.title())
        result += ' ' + weekdays[weekday_index]
        

    # Getting Days Later
    # next day, 2 days later, 3 days later ...


    return result




print(add_time("8:30 PM", "25", 'moNday'))
print(add_time("8:30 PM", "5"))
print(add_time("8:30 PM", "15"))






















