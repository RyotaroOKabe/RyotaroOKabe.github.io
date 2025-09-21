# Enhanced Publications Generator for Academic Pages
# This script generates Jekyll markdown files from a TSV spreadsheet

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

def generate_publications():
    """Generate publication markdown files from TSV."""
    
    # Read the TSV file
    try:
        publications = pd.read_csv("publications.tsv", sep="\t", header=0)
        print(f"Loaded {len(publications)} publications from TSV file")
    except FileNotFoundError:
        print("Error: publications.tsv not found!")
        print("Please create publications.tsv based on publications_template.tsv")
        return
    
    # Process each publication
    for row, item in publications.iterrows():
        
        # Generate filename
        pub_date = str(item.pub_date) if pd.notna(item.pub_date) else "2024-01-01"
        url_slug = str(item.url_slug) if pd.notna(item.url_slug) else "publication"
        
        # Clean url_slug to be filesystem safe
        url_slug = url_slug.replace("https://", "").replace("http://", "").replace("/", "-").replace(":", "").replace("?", "").replace("=", "")
        url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
        if not url_slug:
            url_slug = f"publication-{row}"
        
        md_filename = pub_date + "-" + url_slug + ".md"
        html_filename = pub_date + "-" + url_slug
        
        # Start building markdown content
        md = "---\n"
        md += f'title: "{item.title}"\n'
        md += "collection: publications\n"
        md += f"permalink: /publication/{html_filename}\n"
        
        # Add excerpt if available
        if pd.notna(item.excerpt) and len(str(item.excerpt).strip()) > 5:
            md += f"excerpt: '{html_escape(item.excerpt)}'\n"
        
        # Add date
        md += f"date: {pub_date}\n"
        
        # Add venue
        md += f"venue: '{html_escape(item.venue)}'\n"
        
        # Add category (with smart defaults)
        if pd.notna(item.category) and str(item.category).strip():
            md += f"category: {item.category}\n"
        else:
            # Auto-detect category based on venue
            venue_lower = str(item.venue).lower()
            if any(keyword in venue_lower for keyword in ['journal', 'arxiv', 'nature', 'science']):
                md += "category: manuscripts\n"
            elif any(keyword in venue_lower for keyword in ['conference', 'proceeding', 'symposium']):
                md += "category: conferences\n"
            else:
                md += "category: manuscripts\n"  # default
        
        # Add paper URL
        if pd.notna(item.paper_url) and len(str(item.paper_url).strip()) > 5:
            md += f"paperurl: '{item.paper_url}'\n"
        
        # Add slides URL
        if pd.notna(item.slides_url) and len(str(item.slides_url).strip()) > 5:
            md += f"slidesurl: '{item.slides_url}'\n"
        
        # Add citation
        if pd.notna(item.citation) and len(str(item.citation).strip()) > 5:
            md += f"citation: '{html_escape(item.citation)}'\n"
        
        md += "---\n\n"
        
        # Add content section
        if pd.notna(item.excerpt) and len(str(item.excerpt).strip()) > 5:
            md += f"{html_escape(item.excerpt)}\n\n"
        
        # Add download links
        if pd.notna(item.slides_url) and len(str(item.slides_url).strip()) > 5:
            md += f"[Download slides here]({item.slides_url})\n\n"
        
        if pd.notna(item.paper_url) and len(str(item.paper_url).strip()) > 5:
            md += f"[Download paper here]({item.paper_url})\n\n"
        
        # Add citation
        if pd.notna(item.citation) and len(str(item.citation).strip()) > 5:
            md += f"Recommended citation: {item.citation}\n"
        
        # Write to file
        output_path = f"../_publications/{md_filename}"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md)
        
        print(f"Generated: {md_filename}")
    
    print(f"\nSuccessfully generated {len(publications)} publication files!")

def create_new_publication():
    """Interactive function to create a new publication entry."""
    print("\n=== Create New Publication ===")
    
    title = input("Publication title: ")
    venue = input("Venue (Journal/Conference): ")
    date = input("Publication date (YYYY-MM-DD): ")
    excerpt = input("Brief description (optional): ")
    citation = input("Full citation: ")
    paper_url = input("Paper URL (optional): ")
    slides_url = input("Slides URL (optional): ")
    
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
    
    return {
        'pub_date': date,
        'title': title,
        'venue': venue,
        'excerpt': excerpt,
        'citation': citation,
        'url_slug': url_slug,
        'paper_url': paper_url,
        'slides_url': slides_url,
        'category': category
    }

if __name__ == "__main__":
    print("Enhanced Publications Generator")
    print("==============================")
    
    choice = input("\n1. Generate from TSV\n2. Create new publication\nChoice (1 or 2): ")
    
    if choice == "1":
        generate_publications()
    elif choice == "2":
        new_pub = create_new_publication()
        print("\nNew publication data:")
        for key, value in new_pub.items():
            print(f"{key}: {value}")
        print("\nAdd this to your publications.tsv file and run the generator.")
    else:
        print("Invalid choice!")
