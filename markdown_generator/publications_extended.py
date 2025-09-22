
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a csv of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.csv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard csv format and citation style.
# 

# ## Data format
# 
# The csv needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and paper_url, with a header at the top. 
# 
# - `excerpt` and `paper_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import csv
# 
# Pandas makes this easy with the read_csv function. We are using a csv, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

# publications = pd.read_csv("publications.csv", sep="\t", header=0)
publications = pd.read_csv("publications.csv", header=0)
# print(publications)


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the csv dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

import os
for row, item in publications.iterrows():
    print(item)
    
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publication/""" + html_filename
    
    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"
    
    md += "\ndate: " + str(item.pub_date) 
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"
    
    # Add category field - you can modify this logic based on venue or add a category column to your csv
    if 'journal' in item.venue.lower() or 'arxiv' in item.venue.lower():
        md += "\ncategory: manuscripts"
    elif 'conference' in item.venue.lower() or 'proceeding' in item.venue.lower():
        md += "\ncategory: conferences"
    else:
        md += "\ncategory: manuscripts"  # default to manuscripts
    
    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + item.paper_url + "'"
    
    md += "\ncitation: '" + html_escape(item.citation) + "'"
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    if len(str(item.paper_url)) > 5:
        md += "\n<a href='" + item.paper_url + "'>Paper</a> /" 
    # if len(str(item.media_name)) > 5:
    #     md += "\n<a href='" + item.media_url + "'>" + item.media_name + "</a> /" 
    if len(str(item.media_url)) > 5:
        print(type(item.media_url), item.media_url)
        media_dict = {}
        try:
            # Try to evaluate the string as a dictionary
            if isinstance(item.media_url, str) and item.media_url.strip().startswith("{"):
                import ast
                media_dict = ast.literal_eval(item.media_url)
            elif isinstance(item.media_url, dict):
                media_dict = item.media_url
        except Exception:
            media_dict = {}
        print(type(media_dict), media_dict)
        for media_name, media_url in media_dict.items():
            md += "\n<a href='" + media_url + "'>" + media_name + "</a> /" 
    if len(str(item.github_url)) > 5:
        md += "\n<a href='" + item.github_url + "'>GitHub</a> /" 
    if len(str(item.data_url)) > 5:
        md += "\n<a href='" + item.data_url + "'>Data page</a> /" 
    
    if len(str(item.figure)) > 5:
       ###
        # <a href="https://doi.org/10.1038/s41563-025-02355-y" target="_blank" rel="noopener">
        #   <img src="{{ '/images_pub/okabe2025structural.png' | relative_url }}"
        #        alt="Generated structures illustrating symmetry-aware constraints in SCIGEN"
        #        style="max-width:100%; height:auto; display:block; margin:1rem auto;">
        # </a>
        # generalize the above code
        md += "\n\n<a href='" + item.paper_url + "' target='_blank' rel='noopener'>" 
        md += f"\n\t<img src=" '"{{' + "'images_pub/" + item.figure + ".png' | relative_url" + '}}"' 
        # md += "\nalt='" + item.figure + "'" 
        md += "\n\tstyle='max-width:80%; height:auto; display:block; margin:1rem auto;'>"
        md += "\n</a>"

    md += "\n"
    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"
        
    # md += "\nRecommended citation: " + item.citation
    
    md_filename = os.path.basename(md_filename)
       
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)


