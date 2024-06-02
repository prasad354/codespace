def emojize(text):
    # Dictionary mapping text codes or aliases to emojis
    emoji_dict = {
        ":)": "😊",
        ":(": "😞",
        ":-)": "😊",
        ":-(": "😞",
        ":-D": "😃",
        ":-P": "😛",
        ":heart:": "❤️",
        ":star:": "⭐",
        ":thumbsup:": "👍",
        ":thumbsdown:": "👎",
        # Add more mappings as needed
    }
    
    # Replace text codes with emojis
    for code, emoji in emoji_dict.items():
        text = text.replace(code, emoji)
    
    return text

def main():
    # Prompt the user for input
    user_input = input("Enter a text in English: ")
    
    # Emojize the input text
    emojized_text = emojize(user_input)
    
    # Output the emojized text
    print("Emojized text:")
    print(emojized_text)

# Run the main function
if __name__ == "__main__":
    main()
