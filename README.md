# Secret Message Decoder 

This project extracts and reconstructs a hidden ASCII/Unicode art message from a **published Google Doc**.  
The Google Doc contains a table of **X-coordinate, Character, and Y-coordinate** values.  
The script parses these values, places characters at the right `(x, y)` positions in a 2D grid, and prints the secret message.

---

## Features
- Fetches data from a published Google Docs link.
- Parses coordinates and characters from table rows.
- Builds a grid using **X (columns)** and **Y (rows)** positions.
- Prints the secret message in a fixed-width format.
- Includes axis labels for debugging.

---

## Requirements
Make sure you have Python 3 installed along with:

```bash
pip install requests beautifulsoup4

Usage

Clone this repo:

git clone https://github.com/yourusername/secret-message-decoder.git
cd secret-message-decoder


Run the script with Python:

python decoder.py


Example output (snippet):

   012345678901234567890
0                      
1                      
2          ███         
3          █           
4          ███         

**Project Structure**
.
├── decoder.py   # Main script
├── README.md    # Project documentation

**Example Code (decoder.py)**
import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

header_info = soup.find("div", id="contents")
tds = [td.get_text(strip=True) for td in header_info.find_all("td")]
tds = tds[3:]  # remove table header

rows = [tds[i:i+3] for i in range(0, len(tds), 3)]
points = [(int(r[0]), int(r[2]), r[1]) for r in rows]

max_x = max(x for x, y, ch in points)
max_y = max(y for x, y, ch in points)

grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for x, y, ch in points:
    grid[y][x] = ch

print("   " + "".join([f"{i%10}" for i in range(max_x+1)]))  
for y, row in enumerate(grid):
    print(f"{y:2d} " + "".join(row))

**Output**

When run with the provided Google Doc, this script prints a hidden uppercase secret message using ASCII art.
