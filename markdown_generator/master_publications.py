#!/usr/bin/env python
# Master Publications Generator
# Supports multiple input formats: CSV, TSV, and BibTeX

import pandas as pd
import os
import sys
from pathlib import Path

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

def generate_from_csv():
    """Generate publications from CSV file."""
    try:
        publications = pd.read_csv("publications.csv")
        print(f"✅ Loaded {len(publications)} publications from CSV")
        return publications, "CSV"
    except FileNotFoundError:
        print("❌ publications.csv not found")
        return None, None

def generate_from_tsv():
    """Generate publications from TSV file."""
    try:
        publications = pd.read_csv("publications.tsv", sep="\t")
        print(f"✅ Loaded {len(publications)} publications from TSV")
        return publications, "TSV"
    except FileNotFoundError:
        print("❌ publications.tsv not found")
        return None, None

def generate_from_bibtex():
    """Generate publications from BibTeX files."""
    try:
        from pybtex.database.input import bibtex
        import pybtex.database.input.bibtex
        from time import strptime
        import re
        import html
        
        # Configuration for BibTeX files
        publist = {
            "proceeding": {
                "file" : "proceedings.bib",
                "venuekey": "booktitle",
                "venue-pretext": "In the proceedings of ",
            },
            "journal":{
                "file": "pubs.bib",
                "venuekey" : "journal",
                "venue-pretext" : "",
            } 
        }
        
        all_publications = []
        
        for pubsource in publist:
            if not os.path.exists(publist[pubsource]["file"]):
                print(f"⚠️  {publist[pubsource]['file']} not found, skipping...")
                continue
                
            parser = bibtex.Parser()
            bibdata = parser.parse_file(publist[pubsource]["file"])
            
            for bib_id in bibdata.entries:
                try:
                    b = bibdata.entries[bib_id].fields
                    
                    # Parse date
                    pub_year = str(b.get("year", "2024"))
                    pub_month = "01"
                    pub_day = "01"
                    
                    if "month" in b.keys(): 
                        if len(b["month"]) < 3:
                            pub_month = "0" + b["month"]
                            pub_month = pub_month[-2:]
                        elif b["month"] not in range(12):
                            try:
                                tmnth = strptime(b["month"][:3], '%b').tm_mon   
                                pub_month = "{:02d}".format(tmnth) 
                            except:
                                pub_month = "01"
                        else:
                            pub_month = str(b["month"])
                    
                    if "day" in b.keys(): 
                        pub_day = str(b["day"])
                    
                    pub_date = pub_year + "-" + pub_month + "-" + pub_day
                    
                    # Clean title and create URL slug
                    clean_title = b["title"].replace("{", "").replace("}", "").replace("\\", "").replace(" ", "-")
                    url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title).replace("--", "-")
                    
                    # Build citation
                    citation = ""
                    for author in bibdata.entries[bib_id].persons.get("author", []):
                        citation += author.first_names[0] + " " + author.last_names[0] + ", "
                    
                    citation += "\"" + html_escape(b["title"].replace("{", "").replace("}", "").replace("\\", "")) + ".\""
                    venue = publist[pubsource]["venue-pretext"] + b[publist[pubsource]["venuekey"]].replace("{", "").replace("}", "").replace("\\", "")
                    citation += " " + html_escape(venue) + ", " + pub_year + "."
                    
                    # Create publication entry
                    pub_entry = {
                        'pub_date': pub_date,
                        'title': b["title"].replace("{", "").replace("}", "").replace("\\", ""),
                        'venue': venue,
                        'excerpt': b.get("note", ""),
                        'citation': citation,
                        'url_slug': url_slug,
                        'paper_url': b.get("url", ""),
                        'slides_url': "",
                        'category': 'manuscripts' if 'journal' in venue.lower() else 'conferences'
                    }
                    
                    all_publications.append(pub_entry)
                    print(f"✅ Parsed BibTeX entry: {b['title'][:50]}...")
                    
                except KeyError as e:
                    print(f"⚠️  Missing field {e} in {bib_id}")
                    continue
        
        if all_publications:
            df = pd.DataFrame(all_publications)
            print(f"✅ Loaded {len(all_publications)} publications from BibTeX")
            return df, "BibTeX"
        else:
            print("❌ No publications found in BibTeX files")
            return None, None
            
    except ImportError:
        print("❌ pybtex not installed. Install with: pip install pybtex")
        return None, None

def process_publications(publications_df, source_type):
    """Process publications DataFrame and generate markdown files."""
    
    for row, item in publications_df.iterrows():
        # Handle missing data
        pub_date = str(item.pub_date) if pd.notna(item.pub_date) else "2024-01-01"
        title = str(item.title) if pd.notna(item.title) else f"Publication {row+1}"
        venue = str(item.venue) if pd.notna(item.venue) else "Journal"
        
        # Generate URL slug
        if pd.notna(item.url_slug) and str(item.url_slug).strip():
            url_slug = str(item.url_slug).strip()
        else:
            url_slug = title.lower().replace(' ', '-').replace(':', '').replace(',', '').replace('.', '')
            url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
            if not url_slug:
                url_slug = f"publication-{row+1}"
        
        # Clean url_slug for filesystem
        url_slug = url_slug.replace("https://", "").replace("http://", "").replace("/", "-").replace(":", "").replace("?", "").replace("=", "")
        url_slug = ''.join(c for c in url_slug if c.isalnum() or c == '-')
        
        # Generate filename
        md_filename = pub_date + "-" + url_slug + ".md"
        html_filename = pub_date + "-" + url_slug
        
        # Build markdown content
        md = "---\n"
        md += f'title: "{title}"\n'
        md += "collection: publications\n"
        md += f"permalink: /publication/{html_filename}\n"
        
        # Add excerpt
        if pd.notna(item.excerpt) and len(str(item.excerpt).strip()) > 5:
            md += f"excerpt: '{html_escape(item.excerpt)}'\n"
        
        md += f"date: {pub_date}\n"
        md += f"venue: '{html_escape(venue)}'\n"
        
        # Add category
        if pd.notna(item.category) and str(item.category).strip():
            md += f"category: {item.category}\n"
        else:
            venue_lower = venue.lower()
            if any(keyword in venue_lower for keyword in ['journal', 'arxiv', 'nature', 'science']):
                md += "category: manuscripts\n"
            elif any(keyword in venue_lower for keyword in ['conference', 'proceeding', 'symposium']):
                md += "category: conferences\n"
            else:
                md += "category: manuscripts\n"
        
        # Add URLs
        if pd.notna(item.paper_url) and len(str(item.paper_url).strip()) > 5:
            md += f"paperurl: '{item.paper_url}'\n"
        
        if pd.notna(item.slides_url) and len(str(item.slides_url).strip()) > 5:
            md += f"slidesurl: '{item.slides_url}'\n"
        
        if pd.notna(item.citation) and len(str(item.citation).strip()) > 5:
            md += f"citation: '{html_escape(item.citation)}'\n"
        
        md += "---\n\n"
        
        # Add content
        if pd.notna(item.excerpt) and len(str(item.excerpt).strip()) > 5:
            md += f"{html_escape(item.excerpt)}\n\n"
        
        if pd.notna(item.slides_url) and len(str(item.slides_url).strip()) > 5:
            md += f"[Download slides here]({item.slides_url})\n\n"
        
        if pd.notna(item.paper_url) and len(str(item.paper_url).strip()) > 5:
            md += f"[Download paper here]({item.paper_url})\n\n"
        
        if pd.notna(item.citation) and len(str(item.citation).strip()) > 5:
            md += f"Recommended citation: {item.citation}\n"
        
        # Write file
        output_path = f"../_publications/{md_filename}"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md)
        
        print(f"Generated: {md_filename}")

def main():
    print("🎯 Master Publications Generator")
    print("================================")
    print("Supports: CSV, TSV, and BibTeX formats")
    print()
    
    # Try different sources in order of preference
    publications_df, source_type = generate_from_csv()
    
    if publications_df is None:
        publications_df, source_type = generate_from_tsv()
    
    if publications_df is None:
        publications_df, source_type = generate_from_bibtex()
    
    if publications_df is None:
        print("❌ No publication data found!")
        print("Please create one of the following:")
        print("  - publications.csv")
        print("  - publications.tsv") 
        print("  - pubs.bib and/or proceedings.bib")
        return
    
    print(f"\n📝 Processing {len(publications_df)} publications from {source_type}")
    process_publications(publications_df, source_type)
    print(f"\n✅ Successfully generated {len(publications_df)} publication files!")

if __name__ == "__main__":
    main()
