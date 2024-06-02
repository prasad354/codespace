def get_media_type():
    # Dictionary mapping file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    
    # Prompt the user for the file name
    file_name = input("Enter the name of the file: ").strip().lower()
    
    # Check the file extension and output the corresponding media type
    for ext, media_type in media_types.items():
        if file_name.endswith(ext):
            print(media_type)
            return
    
    # If the file extension is not found, output 'application/octet-stream'
    print("application/octet-stream")

# Run the function
get_media_type()
