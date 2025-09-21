# Enhanced Talks Generator for Academic Pages
# This script generates Jekyll markdown files for talks from a TSV spreadsheet

import pandas as pd
import os
from datetime import datetime

def html_escape(text):
    """Escape special characters for YAML compatibility."""
    if pd.isna(text) or text == '':
        return ''
    
    html_escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&apos;"
    }
    return "".join(html_escape_table.get(c, c) for c in str(text))

def generate_talks():
    """Generate talk markdown files from TSV."""
    
    # Read the TSV file
    try:
        talks = pd.read_csv("talks.tsv", sep="\t", header=0)
        print(f"Loaded {len(talks)} talks from TSV file")
    except FileNotFoundError:
        print("Error: talks.tsv not found!")
        print("Please create talks.tsv based on talks_template.tsv")
        return
    
    # Process each talk
    for row, item in talks.iterrows():
        
        # Generate filename
        md_filename = str(item.date) + "-" + item.url_slug + ".md"
        html_filename = str(item.date) + "-" + item.url_slug
        
        # Start building markdown content
        md = "---\n"
        md += f'title: "{item.title}"\n'
        md += "collection: talks\n"
        
        # Add type (default to "Talk" if not specified)
        talk_type = item.type if pd.notna(item.type) and str(item.type).strip() else "Talk"
        md += f'type: "{talk_type}"\n'
        
        md += f"permalink: /talks/{html_filename}\n"
        
        # Add venue if available
        if pd.notna(item.venue) and len(str(item.venue).strip()) > 3:
            md += f'venue: "{html_escape(item.venue)}"\n'
        
        # Add date
        md += f"date: {item.date}\n"
        
        # Add location if available
        if pd.notna(item.location) and len(str(item.location).strip()) > 3:
            md += f'location: "{html_escape(item.location)}"\n'
        
        md += "---\n\n"
        
        # Add content
        if pd.notna(item.talk_url) and len(str(item.talk_url).strip()) > 3:
            md += f"[More information here]({item.talk_url})\n\n"
        
        if pd.notna(item.description) and len(str(item.description).strip()) > 3:
            md += f"{html_escape(item.description)}\n"
        
        # Write to file
        output_path = f"../_talks/{md_filename}"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md)
        
        print(f"Generated: {md_filename}")
    
    print(f"\nSuccessfully generated {len(talks)} talk files!")

def create_new_talk():
    """Interactive function to create a new talk entry."""
    print("\n=== Create New Talk ===")
    
    title = input("Talk title: ")
    talk_type = input("Type (Talk/Poster/Invited Talk/Tutorial/Conference proceedings talk): ")
    venue = input("Venue/Institution: ")
    date = input("Date (YYYY-MM-DD): ")
    location = input("Location (City, State/Country): ")
    talk_url = input("Talk URL/slides link (optional): ")
    description = input("Description (optional): ")
    
    # Generate URL slug from title
    url_slug = title.lower().replace(' ', '-').replace(':', '').replace(',', '').replace('.', '')
    url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
    
    print(f"\nGenerated URL slug: {url_slug}")
    
    return {
        'title': title,
        'type': talk_type,
        'url_slug': url_slug,
        'venue': venue,
        'date': date,
        'location': location,
        'talk_url': talk_url,
        'description': description
    }

if __name__ == "__main__":
    print("Enhanced Talks Generator")
    print("========================")
    
    choice = input("\n1. Generate from TSV\n2. Create new talk\nChoice (1 or 2): ")
    
    if choice == "1":
        generate_talks()
    elif choice == "2":
        new_talk = create_new_talk()
        print("\nNew talk data:")
        for key, value in new_talk.items():
            print(f"{key}: {value}")
        print("\nAdd this to your talks.tsv file and run the generator.")
    else:
        print("Invalid choice!")
