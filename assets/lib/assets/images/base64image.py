import base64
import sys
import os

def image_to_base64(image_path):
    """
    Convert an image to a Base64 string.

    Parameters:
    - image_path: Path to the image file.

    Returns:
    A Base64 encoded string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        return encoded_string
    except FileNotFoundError:
        print(f"The file '{image_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def save_base64_to_file(base64_string, output_path):
    """
    Save the Base64 string to a file.

    Parameters:
    - base64_string: The Base64 encoded string of the image.
    - output_path: Path where the .b64 file will be saved.
    """
    try:
        with open(output_path, "w") as file:
            file.write(base64_string)
        print(f"Base64 string saved to {output_path}")
    except Exception as e:
        print(f"Failed to save Base64 string to file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_to_base64.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    base64_string = image_to_base64(image_path)

    # Construct the output file name by replacing the original extension with .b64
    output_file_path = os.path.splitext(image_path)[0] + ".b64"
    save_base64_to_file(base64_string, output_file_path)
