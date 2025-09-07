# Ubuntu-Inspired Image Fetcher

**The Wisdom of Ubuntu:** "I am because we are"

## Overview
This Python script embodies the Ubuntu philosophy by connecting to the global community, respectfully fetching shared images from the internet, and organizing them for later appreciation and sharing.

## Features
- Prompts the user for an image URL
- Creates a `Fetched_Images` directory if it doesn't exist
- Downloads the image using the `requests` library
- Saves the image with an appropriate filename
- Handles errors gracefully and respectfully

## Ubuntu Principles
- **Community:** Connects to the wider web community
- **Respect:** Handles errors gracefully without crashing
- **Sharing:** Organizes fetched images for sharing
- **Practicality:** Serves a real need for image organization

## Requirements
- Python 3.x
- `requests` library

## Usage
1. Run the script:
   ```powershell
   python "Python Libraries Assignment.py"
   ```
2. Enter the URL of the image when prompted.
3. The image will be saved in the `Fetched_Images` directory.

## Error Handling
- The script checks for HTTP errors and connection issues.
- If the image cannot be fetched or saved, a respectful message is displayed.

## Example
```
Enter the URL of an image to fetch: https://example.com/image.jpg
Image saved to Fetched_Images/image.jpg
```

## License
This project is for educational purposes and inspired by the Ubuntu philosophy.
