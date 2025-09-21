# CSV Talks Generator for Academic Pages
# This script generates Jekyll markdown files for talks from a CSV spreadsheet

import pandas as pd
import os

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

def generate_talks_from_csv():
    """Generate talk markdown files from CSV."""
    
    # Read the CSV file
    try:
        talks = pd.read_csv("talks.csv")
        print(f"Loaded {len(talks)} talks from CSV file")
    except FileNotFoundError:
        print("Error: talks.csv not found!")
        print("Please create talks.csv with your talk data")
        return
    
    # Process each talk
    for row, item in talks.iterrows():
        
        # Handle missing or invalid data
        date = str(item.date) if pd.notna(item.date) else "2024-01-01"
        title = str(item.title) if pd.notna(item.title) else f"Talk {row+1}"
        
        # Generate URL slug from title if not provided
        if pd.notna(item.url_slug) and str(item.url_slug).strip():
            url_slug = str(item.url_slug).strip()
        else:
            url_slug = title.lower().replace(' ', '-').replace(':', '').replace(',', '').replace('.', '')
            url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
            if not url_slug:
                url_slug = f"talk-{row+1}"
        
        # Clean url_slug for filesystem
        url_slug = url_slug.replace("https://", "").replace("http://", "").replace("/", "-").replace(":", "").replace("?", "").replace("=", "")
        url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
        
        # Generate filename
        md_filename = date + "-" + url_slug + ".md"
        html_filename = date + "-" + url_slug
        
        # Start building markdown content
        md = "---\n"
        md += f'title: "{title}"\n'
        md += "collection: talks\n"
        
        # Add type (default to "Talk" if not specified)
        talk_type = item.type if pd.notna(item.type) and str(item.type).strip() else "Talk"
        md += f'type: "{talk_type}"\n'
        
        md += f"permalink: /talks/{html_filename}\n"
        
        # Add venue if available
        if pd.notna(item.venue) and len(str(item.venue).strip()) > 3:
            md += f'venue: "{html_escape(item.venue)}"\n'
        
        # Add date
        md += f"date: {date}\n"
        
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

if __name__ == "__main__":
    print("CSV Talks Generator")
    print("==================")
    generate_talks_from_csv()
