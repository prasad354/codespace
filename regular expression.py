import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Regular expression to match "um" as a whole word
    regex = r'\bum\b'
    
    # Search for matches using regex
    matches = re.findall(regex, s, flags=re.IGNORECASE)
    
    return len(matches)

if __name__ == "__main__":
    main()
