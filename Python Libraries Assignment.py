import os
import requests
from urllib.parse import urlparse

def fetch_image():
	print("The Wisdom of Ubuntu: 'I am because we are'\n")
	url = input("Enter the URL of an image to fetch: ").strip()
	if not url:
		print("No URL provided. Exiting respectfully.")
		return

	# Create directory for images
	images_dir = "Fetched_Images"
	os.makedirs(images_dir, exist_ok=True)

	# Try to fetch the image
	try:
		response = requests.get(url, stream=True)
		response.raise_for_status()
	except requests.exceptions.RequestException as e:
		print(f"Could not fetch image: {e}")
		return

	# Extract filename from URL
	parsed_url = urlparse(url)
	filename = os.path.basename(parsed_url.path)
	if not filename:
		filename = "image.jpg"
	save_path = os.path.join(images_dir, filename)

	# If file exists, generate a unique name
	base, ext = os.path.splitext(filename)
	counter = 1
	while os.path.exists(save_path):
		filename = f"{base}_{counter}{ext or '.jpg'}"
		save_path = os.path.join(images_dir, filename)
		counter += 1

	# Save image in binary mode
	try:
		with open(save_path, "wb") as f:
			for chunk in response.iter_content(1024):
				f.write(chunk)
		print(f"Image saved to {save_path}")
	except Exception as e:
		print(f"Error saving image: {e}")

if __name__ == "__main__":
	fetch_image()
