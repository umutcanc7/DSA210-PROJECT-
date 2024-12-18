import requests
import csv
from bs4 import BeautifulSoup

def fetch_match_data(url):
    # Define headers to mimic a browser request (optional for some websites)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    
    # Send a GET request to the website
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return []
    
    # Parse the HTML content with BeautifulSoup
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Locate the match data rows
    table_rows = soup.select("tr")
    matches = []

    # Iterate through the rows and extract relevant data
    for row in table_rows:
        # Find the score span inside the anchor tag with class 'ergebnis-link'
        score_anchor = row.find("a", class_="ergebnis-link")
        place_td = row.find_all("td", class_="zentriert")

        if score_anchor and place_td:
            # Extract the score
            score = score_anchor.get_text(strip=True)
            
            # Remove "UZT" if it exists in the right score
            if "UZT" in score:
                score = score.replace("UZT", "").strip()

            # Extract the place (E for home, D for away)
            place = place_td[3].get_text(strip=True) if len(place_td) > 3 else "N/A"
            
            # Initialize the result variable
            result = "N/A"
            
            # Check if it's a draw (both teams have the same score)
            if ":" in score:
                score_parts = score.split(":")
                if len(score_parts) == 2:
                    left_score, right_score = score_parts[0], score_parts[1]
                    
                    # Determine the match result based on scores and location (home/away)
                    if left_score == right_score:
                        result = "Draw"
                    elif place == "E":  # Home match
                        result = "Win" if int(left_score) > int(right_score) else "Loss"
                    elif place == "D":  # Away match
                        result = "Win" if int(left_score) < int(right_score) else "Loss"
            
            # Extract the date (only numeric part, without the day name)
            date = place_td[1].get_text(strip=True) if len(place_td) > 1 else "N/A"
            date_parts = date.split(" ")  # Split by space
            numeric_date = date_parts[-1]  # Get the last part as the numeric date
            
            time = place_td[2].get_text(strip=True) if len(place_td) > 2 else "N/A"
            
            # Create a dictionary for each match with specific columns
            match_data = {
                "Date": numeric_date,
                "Time": time,
                "Score": score,
                "Result": result,
            }
            matches.append(match_data)

    return matches

def save_to_csv(data, filename):
    # Define the column names for the CSV file
    fieldnames = ["Date", "Time", "Score", "Result"]
    
    # Open the CSV file in write mode and create a CSV DictWriter object
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header (column names)
        writer.writeheader()
        
        # Write each match's data in a row under the correct column
        for match in data:
            writer.writerow(match)

if __name__ == "__main__":
    # Replace with the URL of the webpage containing the match data
    url = "https://www.transfermarkt.com.tr/fenerbahce-istanbul/spielplandatum/verein/36"  # Update with the correct URL
    
    # Fetch match data
    match_data = fetch_match_data(url)
    
    if match_data:
        print("Match Data Extracted and Saving to CSV...")
        # Save the extracted data to a CSV file
        save_to_csv(match_data, "match_data.csv")
        print("Data saved to match_data.csv")
    else:
        print("No match data found.")
