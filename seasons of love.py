from datetime import datetime, date

def main():
    birthdate = input("Enter your date of birth (YYYY-MM-DD): ")
    age_minutes = calculate_age_in_minutes(birthdate)
    print("Your age in minutes is:", spell_out(age_minutes))

def calculate_age_in_minutes(birthdate_str):
    try:
        # Convert birthdate string to datetime object
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

        # Get today's date
        today = date.today()

        # Calculate age in days
        age_days = (today - birthdate).days

        # Convert days to minutes
        age_minutes = age_days * 24 * 60

        return age_minutes
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        exit()

def spell_out(minutes):
    # Define words for numbers
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty"]

    # Convert minutes to hours and minutes
    hours = minutes // 60
    minutes %= 60

    # Convert hours and minutes to English words
    hour_str = f"{words[hours]}" if hours < 20 else f"{tens[hours // 10]}{words[hours % 10]}"
    minute_str = f"{words[minutes]}" if minutes < 20 else f"{tens[minutes // 10]}{words[minutes % 10]}"

    if hours == 0:
        return f"{minute_str} minutes"
    elif hours == 1:
        return f"{hour_str} hour {minute_str} minutes"
    else:
        return f"{hour_str} hours {minute_str} minutes"

if __name__ == "__main__":
    main()
