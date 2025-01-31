import random
import csv
import os

# Function to update the quote in the README file
def update_quote():
    # Path to your CSV file (now inside the Quote folder)
    quotes_file = "Quote/quotes.csv"
    
    # Path to your README file
    readme_file = "README.md"
    
    # Read the quotes from the CSV file
    with open(quotes_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        quotes = [row[0] for row in reader]  # Get all the quotes from the first column
    
    # Select a random quote
    quote = random.choice(quotes).strip()
    
    # Read the current content of the README
    with open(readme_file, "r") as f:
        readme_content = f.read()
    
    # Replace the placeholder ![Quote] with the selected quote
    updated_readme_content = readme_content.replace("![Quote]", f'"{quote}"')
    
    # Write the updated content back to README.md
    with open(readme_file, "w") as f:
        f.write(updated_readme_content)
    
    print(f"Updated quote: {quote}")

if __name__ == "__main__":
    update_quote()
