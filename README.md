# 📸 Photo Organizer by Year

This simple Python script organizes your photos into folders by year, based on the original creation date from their EXIF metadata. If EXIF data isn't available, it falls back to the file's last modified time. I created this script because I was trying to organize my current photos and I saw how could I do it more quickly.

## ✅ Features

- Automatically extracts year from EXIF metadata
- Falls back to file modified date when EXIF is missing
- Organizes images into year-based folders
- Supports `.jpg`, `.jpeg`, `.png` files
- Logs all actions to `photo_organizer.log`
- Console-based interface

## 💻 Requirements

- Python 3.6+
- Pillow

Install dependencies:

```bash
pip install -r requirements.txt
