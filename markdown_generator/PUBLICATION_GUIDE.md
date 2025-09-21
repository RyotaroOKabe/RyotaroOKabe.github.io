# 📚 Publication Management Guide

This guide explains how to use all your publication generation scripts effectively.

## 🎯 Quick Start (Recommended)

**Use the Master Script** - it automatically detects your data format:
```bash
python master_publications.py
```

This script will:
1. ✅ Look for `publications.csv` (preferred)
2. ✅ Fall back to `publications.tsv` if CSV not found
3. ✅ Fall back to BibTeX files (`pubs.bib`, `proceedings.bib`) if neither CSV/TSV found

## 📋 Available Scripts & When to Use Them

### 1. 🎯 `master_publications.py` - **RECOMMENDED**
**Best for**: Daily use - automatically handles all formats

**Features**:
- ✅ Supports CSV, TSV, and BibTeX
- ✅ Auto-detects available data sources
- ✅ Smart category detection
- ✅ Robust error handling

**Usage**:
```bash
python master_publications.py
```

### 2. 📊 `csv_publications.py` - CSV Format
**Best for**: When you want to edit in Excel/Google Sheets

**Features**:
- ✅ Easy editing in spreadsheet applications
- ✅ Visual data management
- ✅ Universal compatibility

**Usage**:
```bash
python csv_publications.py
```

### 3. 🔬 `pubsFromBib.py` - BibTeX Integration
**Best for**: If you maintain a BibTeX bibliography

**Setup Required**:
1. Create `pubs.bib` and/or `proceedings.bib` files
2. Update the `publist` dictionary in the script
3. Install pybtex: `pip install pybtex`

**Usage**:
```bash
python pubsFromBib.py
```

### 4. 🛠️ `enhanced_publications.py` - Interactive TSV
**Best for**: When you want interactive content creation

**Features**:
- ✅ Interactive mode for adding new publications
- ✅ Smart category detection
- ✅ Better error handling than simple script

**Usage**:
```bash
python enhanced_publications.py
# Choose option 1 to generate from TSV
# Choose option 2 to interactively add new publication
```

### 5. 📝 `simple_publications.py` - Basic TSV
**Best for**: Quick generation from existing TSV data

**Usage**:
```bash
python simple_publications.py
```

## 🔄 Workflow Recommendations

### For New Users:
1. **Start with CSV**: Use `csv_publications.py`
2. **Edit in Excel**: Open `publications.csv` in Excel/Google Sheets
3. **Regenerate**: Run `python csv_publications.py`

### For BibTeX Users:
1. **Create .bib files**: `pubs.bib`, `proceedings.bib`
2. **Use master script**: `python master_publications.py`
3. **Export to CSV**: For future editing in spreadsheets

### For Power Users:
1. **Use master script**: `python master_publications.py`
2. **Switch formats as needed**: CSV for editing, BibTeX for import
3. **Version control**: Track changes in Git

## 📁 Data Format Requirements

### CSV Format (`publications.csv`):
```csv
pub_date,title,venue,excerpt,citation,url_slug,paper_url,slides_url,category
2024-07-05,"Title","Journal","Description","Citation","url-slug","https://...","https://...","manuscripts"
```

### TSV Format (`publications.tsv`):
```
pub_date	title	venue	excerpt	citation	url_slug	paper_url	slides_url	category
2024-07-05	Title	Journal	Description	Citation	url-slug	https://...	https://...	manuscripts
```

### BibTeX Format (`pubs.bib`):
```bibtex
@article{okabe2024structural,
  title={Structural Constraint Integration in Generative Model for Discovery of Quantum Material Candidates},
  author={Okabe, Ryotaro and others},
  journal={arXiv preprint arXiv:2407.04557},
  year={2024},
  url={https://arxiv.org/abs/2407.04557}
}
```

## 🎨 Category System

Your publications are automatically categorized:

- **`manuscripts`**: Journal articles, arXiv preprints, Nature/Science papers
- **`conferences`**: Conference proceedings, symposium papers
- **`books`**: Book chapters, monographs

Categories are auto-detected based on venue names, or you can specify them manually.

## 🚀 Pro Tips

### 1. **Use the Master Script**
```bash
# This handles everything automatically
python master_publications.py
```

### 2. **Edit in Spreadsheets**
- Open `publications.csv` in Excel/Google Sheets
- Add new publications easily
- Use sorting and filtering
- Regenerate with: `python csv_publications.py`

### 3. **BibTeX Integration**
```bash
# Install BibTeX support
pip install pybtex

# Create your .bib files
# Run master script - it will auto-detect BibTeX
python master_publications.py
```

### 4. **Version Control**
```bash
# Track your data files
git add publications.csv talks.csv
git commit -m "Update publications"
```

### 5. **Backup Your Data**
Keep copies of your CSV/TSV files - they're your source of truth!

## 🔧 Troubleshooting

### "No publications found"
- Check file names: `publications.csv`, `publications.tsv`, `pubs.bib`
- Ensure files are in the `markdown_generator/` directory

### "pybtex not installed"
```bash
pip install pybtex
```

### "Invalid characters in filename"
- The scripts automatically clean URL slugs
- Special characters are converted to safe alternatives

### "Category not detected"
- Add `category` column to your CSV/TSV
- Or let the script auto-detect based on venue names

## 📊 Summary

| Script | Best For | Input Format | Complexity |
|--------|----------|--------------|------------|
| `master_publications.py` | **Daily use** | CSV/TSV/BibTeX | ⭐⭐ |
| `csv_publications.py` | Spreadsheet editing | CSV | ⭐ |
| `pubsFromBib.py` | BibTeX integration | BibTeX | ⭐⭐⭐ |
| `enhanced_publications.py` | Interactive editing | TSV | ⭐⭐ |
| `simple_publications.py` | Quick generation | TSV | ⭐ |

**Recommendation**: Use `master_publications.py` for everything - it's the most flexible and user-friendly option! 🎯
