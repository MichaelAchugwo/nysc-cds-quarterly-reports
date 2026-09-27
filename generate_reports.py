#!/usr/bin/env python3
"""
NYSC CDS Reports Generator
Compiles HTML report sources from _sources/ into publication-ready PDFs.
Works across Windows, macOS, and Linux using headless Chrome / Chromium / Edge.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

REPORTS = [
    {
        "source": "_sources/DLC THIRD QUARTER REPORT 2026.html",
        "output": "DLC THIRD QUARTER REPORT 2026.pdf"
    },
    {
        "source": "_sources/DLC KPI THIRD QUARTER REPORT 26.html",
        "output": "DLC KPI THIRD QUARTER REPORT 26.pdf"
    },
    {
        "source": "_sources/ENVIRONMENTAL CDS THIRD QUARTER REPORT 2026.html",
        "output": "ENVIRONMENTAL CDS THIRD QUARTER REPORT 2026.pdf"
    },
    {
        "source": "_sources/ENVIRONMENTAL CDS KPI THIRD QUARTER REPORT 26.html",
        "output": "ENVIRONMENTAL CDS KPI THIRD QUARTER REPORT 26.pdf"
    }
]

def find_browser():
    candidates = [
        # Environment overrides
        os.environ.get("CHROME_PATH"),
        os.environ.get("BROWSER_PATH"),
        # PATH lookups
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        shutil.which("chrome"),
        shutil.which("msedge"),
        shutil.which("edge"),
        # Windows standard locations
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        # macOS standard locations
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
    ]
    for c in candidates:
        if c and Path(c).is_file():
            return str(Path(c).resolve())
    return None

def build_pdf(browser_path, src_path, dest_path):
    src_abs = Path(src_path).resolve()
    dest_abs = Path(dest_path).resolve()
    
    file_url = src_abs.as_uri()
    print(f"Rendering: {dest_path} from {src_path}...")
    
    cmd = [
        browser_path,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={str(dest_abs)}",
        file_url
    ]
    
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0 and dest_abs.exists():
        print(f" [OK] Generated: {dest_path} ({dest_abs.stat().st_size:,} bytes)")
        return True
    else:
        print(f" [ERROR] Failed to generate {dest_path}")
        if res.stderr:
            print(res.stderr.decode("utf-8", errors="ignore"))
        return False

def main():
    root = Path(__file__).resolve().parent
    os.chdir(root)
    
    browser = find_browser()
    if not browser:
        print("ERROR: No compatible headless browser (Chrome / Chromium / Edge) found in PATH or standard directories.")
        print("You can open the HTML files in '_sources/' directly in any browser and use 'Print -> Save as PDF'.")
        sys.exit(1)
        
    print(f"Using browser: {browser}")
    print(f"Generating {len(REPORTS)} official NYSC CDS PDF reports...\n")
    
    success = True
    for item in REPORTS:
        src = root / item["source"]
        dest = root / item["output"]
        if not src.exists():
            print(f" [WARN] Missing source file: {src}")
            continue
        if not build_pdf(browser, src, dest):
            success = False

    if success:
        print("\nAll reports compiled successfully!")
    else:
        print("\nSome reports failed to compile.")
        sys.exit(1)

if __name__ == "__main__":
    main()
