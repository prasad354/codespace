import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match the time formats
    regex = r'(\d{1,2}):(\d{2}) (AM|PM)'
    
    # Search for matches using regex
    match = re.findall(regex, s)
    
    if not match or len(match) != 2:
        raise ValueError("Invalid input format")

    hours = []
    for time in match:
        hour = int(time[0])
        minute = int(time[1])
        period = time[2]

        if period == "AM":
            if hour == 12:
                hour = 0
        else:
            if hour != 12:
                hour += 12

        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            raise ValueError("Invalid time")

        hours.append(f"{hour:02d}:{minute:02d}")

    return " to ".join(hours)

if __name__ == "__main__":
    main()
