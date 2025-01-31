import requests
from bs4 import BeautifulSoup

def scrape_nasa_article(url, output_file):
    """
    Scrapes the main content from the given NASA webpage, cleans the text, 
    and saves it to a file for further processing.
    """
    try:
        # Send a GET request to fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the main content of the article
        article_content = soup.find("article")  # Look for an article tag
        
        if not article_content:
            print("Error: Could not find the article content on the page.")
            return

        # Extract all paragraph text
        paragraphs = article_content.find_all("p")
        cleaned_text = "\n\n".join([para.get_text(strip=True) for para in paragraphs])

        # Save cleaned text to file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(cleaned_text)

        print(f"✅ Successfully scraped and saved content to '{output_file}'")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    nasa_url = "https://www.nasa.gov/universe/6-things-to-know-about-spherex-nasas-newest-space-telescope/"
    output_filename = "Selected_Document.txt"
    
    scrape_nasa_article(nasa_url, output_filename)
