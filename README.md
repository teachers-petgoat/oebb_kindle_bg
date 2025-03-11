# README

## Overview

This script generates an image displaying real-time departure information for trains from Tullnerfeld station using data from the ÖBB API. The image is formatted to be displayed on a Kindle e-reader.

## How It Works

- The script retrieves live departure data from the ÖBB API.
- The data is parsed and processed to extract relevant train information.
- The script generates a grayscale image using the Python Imaging Library (PIL), containing departure times, delays, train names, destinations, and platform numbers.
- The image is saved and rotated 90 degrees for proper Kindle display.

## Prerequisites

- Python 3
- Required Python packages:
  - `PIL` (Pillow)
  - `requests`
  - `json`
  - `datetime`
  - `html`
- A Kindle device capable of displaying images.
- A web server (such as Apache or Nginx) to serve the generated image.

## Installation

1. Install required Python packages if not already installed:
   ```sh
   pip install pillow requests
   ```
2. Ensure the required font file is available:
   - The script uses `arial.ttf`. If not available, install it or modify the script to use a different font.
3. Set up a web server to serve the image files:
   - Place the images in `/var/www/html/oebb/` (adjust path as needed).

## Usage

1. Run the script using:
   ```sh
   ./script.py
   ```
2. The script generates two images:
   - `90grad.png` (original layout)
   - `status.png` (rotated for Kindle display)
3. Access the image via the web server to display it on the Kindle.

## Script Breakdown

- **Fetching Data:** The script sends a request to the ÖBB API and extracts JSON data.
- **Processing Data:** The script filters out bus departures and extracts train-related details.
- **Generating Image:**
  - A blank 800x600 grayscale image is created.
  - Departure information is drawn onto the image using the `ImageDraw` module.
- **Saving and Rotating Image:**
  - The image is saved as `90grad.png`.
  - The image is then rotated 90° and saved as `status.png` for Kindle compatibility.

## Customization

- **Modify Displayed Data:**
  - Adjust the keys in `journey` to display additional or fewer details.
- **Change Font and Size:**
  - Modify `fnt = ImageFont.truetype('/usr/share/fonts/truetype/arial.ttf', 30)` to use a different font.
- **Adjust Image Size:**
  - Change `Image.new('L', (800, 600))` for different resolutions.
- **Change API Endpoint:**
  - Modify the `link` variable to fetch data for different stations.

## Troubleshooting

- **Missing Font:** Ensure `arial.ttf` is available or replace it with another font.
- **Invalid API Response:** If the API format changes, update the JSON parsing accordingly.
- **Image Not Displaying on Kindle:** Check that the Kindle supports the image format and that it is accessible via the web server.

## License

This project is open-source and can be modified as needed.

