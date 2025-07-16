import os  # For interacting with the file system
import shutil  # For moving files
from PIL import Image  # For opening images
from PIL.ExifTags import TAGS  # For readable EXIF tag names
from datetime import datetime  # For working with file modification dates
import logging  # For logging events to a file

# -----------------------
# Logging configuration
# -----------------------
# Creates a log file 'photo_organizer.log' to record moved files and errors
logging.basicConfig(
    filename='photo_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# -----------------------------------------------------
# Function: Extracts the year from the image's EXIF data
# -----------------------------------------------------
def get_exif_creation_year(image_path):
    try:
        image = Image.open(image_path)  # Open the image file
        exif_data = image._getexif()  # Get EXIF metadata
        if not exif_data:
            return None  # No EXIF data found
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id)  # Convert tag ID to name
            if tag == 'DateTimeOriginal':
                return value.split(":")[0]  # Extract the year (e.g., "2020")
    except Exception as e:
        logging.warning(f"Error reading EXIF from {image_path}: {e}")  # Log any issue
    return None  # Fallback if no EXIF date available

# ----------------------------------------------------
# Function: Organizes photos into folders by year
# ----------------------------------------------------
def organize_photos_by_year(source_folder):
    for filename in os.listdir(source_folder):  # Loop through all files in the folder
        file_path = os.path.join(source_folder, filename)

        # Check if it's an image file
        if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Try to get the year from EXIF metadata
            year = get_exif_creation_year(file_path)

            # If EXIF is missing, fallback to file modification date
            if not year:
                mod_time = os.path.getmtime(file_path)
                year = str(datetime.fromtimestamp(mod_time).year)

            # Create the target folder for that year if it doesn't exist
            year_folder = os.path.join(source_folder, year)
            os.makedirs(year_folder, exist_ok=True)

            # Set the destination path
            new_path = os.path.join(year_folder, filename)

            try:
                # Move the file
                shutil.move(file_path, new_path)
                log_msg = f"Moved: {file_path} -> {new_path}"
                logging.info(log_msg)  # Log the move
                print(log_msg)  # Show progress in the terminal
            except Exception as e:
                # Log and display any move errors
                error_msg = f"Failed to move {file_path}: {e}"
                logging.error(error_msg)
                print(error_msg)

# ---------------------------------------------
# Entry point: runs when script is executed
# ---------------------------------------------
if __name__ == "__main__":
    # Ask the user for the photo folder path
    folder = input("Enter the full path to your photo folder: ").strip()

    # Check if the folder exists and process it
    if os.path.isdir(folder):
        organize_photos_by_year(folder)
        print("Done organizing photos by year.")
    else:
        print("Invalid folder path.")  # Error message for invalid input
