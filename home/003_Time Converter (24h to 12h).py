"""
You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format.

example

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).

Precondition:
'00:00' <= time <= '23:59'
"""


def time_converter(time):
    time = time.split(":")
    if 00 < int(time[0]) <= 10:
             time = time[0].strip("0") + ":" + time[1] + ' a.m.'
    elif int(time[0]) == 11:
             time = str(int(time[0])) + ":" + time[1] + ' a.m.'
    elif int(time[0]) == 12:
             time = str(int(time[0])) + ":" + time[1] + ' p.m.'
    elif int(time[0]) == 00:
             time = '12:00 a.m.'
    else:
             time = str(int(time[0])-12) + ":" + time[1] + ' p.m.'
    return time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
"""
Best solution
"""
from datetime import datetime

def time_converter(time: str) -> str:
    """
        convert the time from the 24-h format into 12-h format
        :param time: in a 24-hour format (as a string)
                    ('12:30', '9:00', '23:15')
        :return: time in a 12-hour format (as a string)
                  ('12:30 p.m.', '9:00 a.m.', 11:15 p.m.)
    """

    d = datetime.strptime(time, "%H:%M")
    t = d.strftime("%I:%M %p")
    am = t[-2:]
    t = t[:-2] + 'a.m.' if am == 'AM' else t[:-2] + 'p.m.'
    h = t[:2]
    if int(h) <= 9: 
        t = h[1] + t[2:]
    return t
    

