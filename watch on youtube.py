import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to match YouTube URLs in src attribute of iframe element
    regex = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([^/"]+)".*?>'

    # Search for the YouTube URL using regex
    match = re.search(regex, s)

    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
