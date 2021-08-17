seconds_in_minutes = 60
seconds_in_hours = 3600

seconds = int(input("Enter seconds :"))

#converting hour from seconds
hours = seconds // 3600
if hours!=0:
    if hours == 1:
        print(hours,"hour", end= " ")
    else:
        print(hours,"hours", end= " ")

#remaining seconds after the hours are accounted for
seconds = seconds % 3600

#converting minutes for remaining seconds after the hours are accounted for
minutes = seconds // 60
if minutes!=0:
    if minutes == 1:
        print(minutes,"minute", end= " ")
    else:
        print(minutes,"minutes", end = " ")

#remaining seconds afther the minutes are accouted for
seconds = seconds % 60
if seconds!=0:
    if seconds == 1:
        print(seconds,"second", end= " ")
    else:
        print(seconds,"seconds", end= " ")

#print(hours, "hours", minutes, "minutes", seconds, "seconds")

