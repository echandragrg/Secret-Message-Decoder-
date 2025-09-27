import requests
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

header_info = soup.find("div", id="contents")

tds = [td.get_text(strip=True) for td in header_info.find_all("td")]
tds = tds[3:]  

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
