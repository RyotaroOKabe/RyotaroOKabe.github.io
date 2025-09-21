# Simple Publications Generator
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

# Read the TSV file
publications = pd.read_csv("publications.tsv", sep="\t", header=0)
print(f"Loaded {len(publications)} publications from TSV file")

# Process each publication
for row, item in publications.iterrows():
    
    # Handle missing or invalid data
    pub_date = str(item.pub_date) if pd.notna(item.pub_date) else "2024-01-01"
    title = str(item.title) if pd.notna(item.title) else f"Publication {row+1}"
    venue = str(item.venue) if pd.notna(item.venue) else "Journal"
    
    # Generate URL slug from title if not provided
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
    
    # Start building markdown content
    md = "---\n"
    md += f'title: "{title}"\n'
    md += "collection: publications\n"
    md += f"permalink: /publication/{html_filename}\n"
    
    # Add excerpt if available
    if pd.notna(item.excerpt) and len(str(item.excerpt).strip()) > 5:
        md += f"excerpt: '{html_escape(item.excerpt)}'\n"
    
    # Add date
    md += f"date: {pub_date}\n"
    
    # Add venue
    md += f"venue: '{html_escape(venue)}'\n"
    
    # Add category (with smart defaults)
    if pd.notna(item.category) and str(item.category).strip():
        md += f"category: {item.category}\n"
    else:
        # Auto-detect category based on venue
        venue_lower = venue.lower()
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
