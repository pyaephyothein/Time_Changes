seconds_in_minutes = 60
seconds_in_hours = 3600

seconds = int(input("Enter seconds: "))

# Converting hours from seconds
hours = seconds // seconds_in_hours
if hours != 0:
    if hours == 1:
        print(hours, "hour", end=" ")
    else:
        print(hours, "hours", end=" ")

# Remaining seconds after the hours are accounted for
seconds = seconds % seconds_in_hours

# Converting minutes from remaining seconds
minutes = seconds // seconds_in_minutes
if minutes != 0:
    if minutes == 1:
        print(minutes, "minute", end=" ")
    else:
        print(minutes, "minutes", end=" ")

# Remaining seconds after the minutes are accounted for
seconds = seconds % seconds_in_minutes
if seconds != 0:
    if seconds == 1:
        print(seconds, "second", end=" ")
    else:
        print(seconds, "seconds", end=" ")

# Handle case where input is exactly 0 seconds
if hours == 0 and minutes == 0 and seconds == 0:
    print("0 seconds")
