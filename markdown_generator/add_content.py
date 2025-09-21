# Interactive Content Addition Script
# This script helps you add new publications or talks to your CSV files

import pandas as pd
import os

def add_publication():
    """Interactive function to add a new publication."""
    print("\n=== Add New Publication ===")
    
    title = input("Publication title: ")
    venue = input("Venue (Journal/Conference): ")
    date = input("Publication date (YYYY-MM-DD): ")
    excerpt = input("Brief description (optional): ")
    citation = input("Full citation: ")
    paper_url = input("Paper URL (optional): ")
    slides_url = input("Slides URL (optional): ")
    github_url = input("GitHub repository URL (optional): ")
    database_url = input("Database page URL (optional): ")
    figure = input("Figure filename (in images/ folder, optional): ")
    
    # Generate URL slug from title
    url_slug = title.lower().replace(' ', '-').replace(':', '').replace(',', '').replace('.', '')
    url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
    
    # Auto-detect category
    venue_lower = venue.lower()
    if any(keyword in venue_lower for keyword in ['journal', 'arxiv', 'nature', 'science']):
        category = 'manuscripts'
    elif any(keyword in venue_lower for keyword in ['conference', 'proceeding', 'symposium']):
        category = 'conferences'
    else:
        category = 'manuscripts'
    
    print(f"\nGenerated URL slug: {url_slug}")
    print(f"Detected category: {category}")
    
    # Create new row data
    new_row = {
        'pub_date': date,
        'title': title,
        'venue': venue,
        'excerpt': excerpt,
        'citation': citation,
        'url_slug': url_slug,
        'paper_url': paper_url,
        'slides_url': slides_url,
        'category': category,
        'github_url': github_url,
        'database_url': database_url,
        'figure': figure
    }
    
    # Read existing CSV and append new row
    try:
        df = pd.read_csv('publications.csv')
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv('publications.csv', index=False)
        print(f"\n✅ Added publication to publications.csv")
        print("Run 'python csv_publications.py' to generate the markdown file.")
    except FileNotFoundError:
        print("❌ publications.csv not found!")
        print("Please create publications.csv first using the template.")

def add_talk():
    """Interactive function to add a new talk."""
    print("\n=== Add New Talk ===")
    
    title = input("Talk title: ")
    talk_type = input("Type (Talk/Poster/Invited Talk/Tutorial): ")
    venue = input("Venue/Institution: ")
    date = input("Date (YYYY-MM-DD): ")
    location = input("Location (City, State/Country): ")
    talk_url = input("Talk URL/slides link (optional): ")
    description = input("Description (optional): ")
    
    # Generate URL slug from title
    url_slug = title.lower().replace(' ', '-').replace(':', '').replace(',', '').replace('.', '')
    url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
    
    print(f"\nGenerated URL slug: {url_slug}")
    
    # Create new row data
    new_row = {
        'title': title,
        'type': talk_type,
        'url_slug': url_slug,
        'venue': venue,
        'date': date,
        'location': location,
        'talk_url': talk_url,
        'description': description
    }
    
    # Read existing CSV and append new row
    try:
        df = pd.read_csv('talks.csv')
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv('talks.csv', index=False)
        print(f"\n✅ Added talk to talks.csv")
        print("Run 'python csv_talks.py' to generate the markdown file.")
    except FileNotFoundError:
        print("❌ talks.csv not found!")
        print("Please create talks.csv first using the template.")

def main():
    print("Content Addition Tool")
    print("====================")
    print("1. Add Publication")
    print("2. Add Talk")
    print("3. Exit")
    
    choice = input("\nChoose an option (1-3): ")
    
    if choice == "1":
        add_publication()
    elif choice == "2":
        add_talk()
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
