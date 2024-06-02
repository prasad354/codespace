import re

def format_date(date_input):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Check if the input matches the "month day, year" format
    date_match = re.match(r"(\w+) (\d{1,2}), (\d{4})", date_input)
    
    if date_match:
        month_str, day_str, year_str = date_match.groups()
        month = months.index(month_str) + 1
        return f"{year_str}-{month:02d}-{day_str.zfill(2)}"
    
    # Check if the input matches the "month/day/year" format
    date_match = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", date_input)
    
    if date_match:
        month_str, day_str, year_str = date_match.groups()
        return f"{year_str}-{month_str.zfill(2)}-{day_str.zfill(2)}"

    return None

def main():
    print("Please enter a date (in the format 'month day, year' or 'month/day/year'): ")
    
    while True:
        date_input = input().strip()
        formatted_date = format_date(date_input)
        
        if formatted_date:
            print(f"The formatted date is: {formatted_date}")
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()
