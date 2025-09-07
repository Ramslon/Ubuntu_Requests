import requests
import requests
import os
from urllib.parse import urlparse
import hashlib

def is_image_content_type(headers):
	content_type = headers.get('Content-Type', '')
	return content_type.startswith('image/')

def get_image_hash(content):
	return hashlib.sha256(content).hexdigest()

def main():
	print("Welcome to the Ubuntu Image Fetcher")
	print("A tool for mindfully collecting images from the web\n")
	print("Precautions: Download only from trusted sources. Avoid running or opening unknown files.\n")

	# Get multiple URLs from user
	urls = input("Enter image URLs separated by commas: ").split(',')
	urls = [u.strip() for u in urls if u.strip()]
	if not urls:
		print("No URLs provided. Exiting.")
		return

	os.makedirs("Fetched_Images", exist_ok=True)

	# Track hashes to prevent duplicates
	existing_hashes = set()
	for fname in os.listdir("Fetched_Images"):
		fpath = os.path.join("Fetched_Images", fname)
		if os.path.isfile(fpath):
			try:
				with open(fpath, 'rb') as f:
					existing_hashes.add(get_image_hash(f.read()))
			except Exception:
				continue

	for url in urls:
		print(f"\nProcessing: {url}")
		try:
			# Use safe headers
			headers = {
				'User-Agent': 'UbuntuImageFetcher/1.0',
				'Accept': 'image/*'
			}
			response = requests.get(url, timeout=10, headers=headers, stream=True)
			response.raise_for_status()

			# Check important HTTP headers
			if not is_image_content_type(response.headers):
				print("✗ Skipped: Content-Type is not an image.")
				continue
			content_length = response.headers.get('Content-Length')
			if content_length and int(content_length) > 10*1024*1024:
				print("✗ Skipped: Image too large (>10MB).")
				continue

			# Read image content
			image_content = response.content
			image_hash = get_image_hash(image_content)
			if image_hash in existing_hashes:
				print("✗ Skipped: Duplicate image detected.")
				continue

			# Extract filename from URL or generate one
			parsed_url = urlparse(url)
			filename = os.path.basename(parsed_url.path)
			if not filename:
				filename = f"downloaded_image_{image_hash[:8]}.jpg"
			filepath = os.path.join("Fetched_Images", filename)

			# Prevent filename collision
			base, ext = os.path.splitext(filename)
			counter = 1
			while os.path.exists(filepath):
				filename = f"{base}_{counter}{ext or '.jpg'}"
				filepath = os.path.join("Fetched_Images", filename)
				counter += 1

			# Save the image
			with open(filepath, 'wb') as f:
				f.write(image_content)
			existing_hashes.add(image_hash)

			print(f"✓ Successfully fetched: {filename}")
			print(f"✓ Image saved to {filepath}")
			print("Connection strengthened. Community enriched.")

		except requests.exceptions.RequestException as e:
			print(f"✗ Connection error: {e}")
		except Exception as e:
			print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
	main()
