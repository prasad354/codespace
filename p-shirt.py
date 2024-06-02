import sys
from PIL import Image

def overlay_shirt(input_image, output_image):
    try:
        # Open the input and shirt images
        input_img = Image.open(input_image)
        shirt_img = Image.open("shirt.png")  # Assuming shirt.png is in the same directory

        # Resize and crop the input image to match the shirt image size
        input_img = input_img.resize(shirt_img.size, Image.ANTIALIAS)

        # Create a new image with transparent background for the result
        result_img = Image.new("RGBA", shirt_img.size)

        # Paste the input image onto the result image (overlaying the shirt)
        result_img.paste(input_img, (0, 0), input_img)

        # Save the result image
        result_img.save(output_image)

        print("Shirt overlay completed.")

    except FileNotFoundError:
        sys.exit("File not found.")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_image.jpg> <output_image.jpg>")

    input_image = sys.argv[1]
    output_image = sys.argv[2]

    overlay_shirt(input_image, output_image)

if __name__ == "__main__":
    main()
