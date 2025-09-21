# run: python fix_utf8.py
import pathlib

def decode_best(b):
    for enc in ("utf-8", "utf-8-sig", "cp932", "cp1252", "latin1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    return b.decode("utf-8", errors="replace")

for p in pathlib.Path("_publications").glob("*.md"):
    b = p.read_bytes()
    s = decode_best(b).replace("\r\n", "\n")  # normalize newlines
    p.write_text(s, encoding="utf-8", newline="\n")
    print("Rewrote as UTF-8:", p)
