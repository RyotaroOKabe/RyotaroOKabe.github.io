# CSV-Based Content Management

This directory contains tools for managing your academic website content using CSV files instead of TSV files.

## Files

### CSV Data Files
- `publications.csv` - Your publications data
- `talks.csv` - Your talks and presentations data

### CSV Template Files
- `publications_template.csv` - Template for adding new publications
- `talks_template.csv` - Template for adding new talks

### Scripts
- `csv_publications.py` - Generate publication markdown files from CSV
- `csv_talks.py` - Generate talk markdown files from CSV
- `add_content.py` - Interactive tool to add new content

## How to Use

### 1. Add New Publications

**Option A: Edit CSV directly**
1. Open `publications.csv` in Excel, Google Sheets, or any CSV editor
2. Add a new row with your publication data
3. Run: `python csv_publications.py`

**Option B: Use interactive tool**
1. Run: `python add_content.py`
2. Choose option 1 (Add Publication)
3. Follow the prompts
4. Run: `python csv_publications.py`

### 2. Add New Talks

**Option A: Edit CSV directly**
1. Open `talks.csv` in Excel, Google Sheets, or any CSV editor
2. Add a new row with your talk data
3. Run: `python csv_talks.py`

**Option B: Use interactive tool**
1. Run: `python add_content.py`
2. Choose option 2 (Add Talk)
3. Follow the prompts
4. Run: `python csv_talks.py`

### 3. Generate All Content

To regenerate all markdown files from your CSV data:

```bash
python csv_publications.py
python csv_talks.py
```

## CSV Format

### Publications CSV Columns
- `pub_date` - Publication date (YYYY-MM-DD)
- `title` - Publication title
- `venue` - Journal/Conference name
- `excerpt` - Brief description (optional)
- `citation` - Full citation
- `url_slug` - URL-friendly identifier (auto-generated if empty)
- `paper_url` - Link to paper (optional)
- `slides_url` - Link to slides (optional)
- `category` - manuscripts/conferences/books (auto-detected if empty)

### Talks CSV Columns
- `title` - Talk title
- `type` - Talk/Poster/Invited Talk/Tutorial
- `url_slug` - URL-friendly identifier (auto-generated if empty)
- `venue` - Institution/Conference name
- `date` - Talk date (YYYY-MM-DD)
- `location` - City, State/Country
- `talk_url` - Link to talk info/slides (optional)
- `description` - Talk description (optional)

## Benefits of CSV Format

✅ **Easy to edit** in Excel, Google Sheets, or any spreadsheet application
✅ **Widely supported** by all data analysis tools
✅ **Better handling** of special characters and commas in text
✅ **Visual editing** - see all your content in a table format
✅ **Sorting and filtering** capabilities in spreadsheet applications
✅ **Version control friendly** - easier to track changes in Git

## Migration from TSV

Your original TSV files have been converted to CSV format:
- `publications.tsv` → `publications.csv`
- `talks.tsv` → `talks.csv`

The TSV files are kept for backup, but you should use the CSV files going forward.
