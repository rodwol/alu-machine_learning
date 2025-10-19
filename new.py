import requests
from bs4 import BeautifulSoup

def print_unicode_grid(google_doc_url: str):
    """
    Fetch a published Google Doc table of x, character, y data and print the Unicode grid.
    """
    response = requests.get(google_doc_url)
    response.raise_for_status()
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    # Extract rows from the first table found
    rows = soup.find_all("tr")
    coords = []

    # Skip header row if present
    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
        try:
            x = int(cells[0].get_text(strip=True))
            char = cells[1].get_text(strip=True)
            y = int(cells[2].get_text(strip=True))
            coords.append((x, y, char))
        except ValueError:
            continue

    if not coords:
        print("No valid coordinates found in document.")
        return

    # Determine grid size
    max_x = max(x for x, _, _ in coords)
    max_y = max(y for _, y, _ in coords)

    # Create and fill grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y, char in coords:
        grid[y][x] = char

    # Print the grid
    for row in grid:
        print("".join(row))

# Example usage:
print_unicode_grid("https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub")
