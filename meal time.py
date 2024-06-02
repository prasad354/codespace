def meal_time():
    # Prompt the user for the time
    time_input = input("Enter the time in 24-hour format (HH:MM): ").strip()
    
    # Extract hours and minutes from the input
    try:
        hours, minutes = map(int, time_input.split(":"))
    except ValueError:
        print("Invalid time format")
        return
    
    # Check if the time is within the breakfast, lunch, or dinner range
    if 7 <= hours < 8 or (hours == 8 and minutes == 0):
        print("It's breakfast time")
    elif 12 <= hours < 13 or (hours == 13 and minutes == 0):
        print("It's lunch time")
    elif 18 <= hours < 19 or (hours == 19 and minutes == 0):
        print("It's dinner time")

# Run the function
meal_time()
