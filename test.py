# save as fix_utf8.py and run: python fix_utf8.py
import pathlib

def read_best(bytes_):
    # try common encodings first
    for enc in ("utf-8", "utf-8-sig", "cp932", "cp1252", "latin1"):
        try:
            return bytes_.decode(enc)
        except UnicodeDecodeError:
            continue
    # last resort: replace bad bytes
    return bytes_.decode("utf-8", errors="replace")

root = pathlib.Path("_publications")
for p in root.glob("*.md"):
    b = p.read_bytes()
    s = read_best(b)
    # normalize to UTF-8 and LF newlines
    s = s.replace("\r\n", "\n")
    p.write_text(s, encoding="utf-8", newline="\n")
    print("Rewrote as UTF-8:", p)
