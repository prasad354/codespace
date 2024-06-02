import sys
import csv

def clean_names(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            students = [row for row in reader]

        cleaned_students = []
        for student in students:
            full_name = student[0].strip('"')
            last_name, first_name = full_name.split(", ")
            cleaned_students.append([first_name, last_name, student[1]])

        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["first", "last", "house"])
            writer.writerows(cleaned_students)

    except FileNotFoundError:
        sys.exit("File not found.")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py <input_file.csv> <output_file.csv>")
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_names(input_file, output_file)
    print("Conversion completed successfully.")

if __name__ == "__main__":
    main()
