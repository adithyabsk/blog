#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
# "requests==2.32.3",
# ]
# ///
"""Sets up KaTeX to a pinned version with all necessary files and configurations.

How to debug KaTeX, copy this to any file:
https://katex.org/docs/issues

```
<style>
  .katex-version {display: none;}
  .katex-version::after {content:"0.10.2 or earlier";}
</style>
<span class="katex">
  <span class="katex-mathml">The KaTeX stylesheet is not loaded!</span>
  <span class="katex-version rule">KaTeX stylesheet version: </span>
</span>
```

"""

import requests
from pathlib import Path

# KaTeX version to use
KATEX_VERSION = "0.16.22"

# Paths
STATIC_DIR = Path("static")
FONTS_DIR = STATIC_DIR / "fonts"
STYLES_DIR = Path("sass")

# CDN URLs for KaTeX files
CDN_BASE = f"https://cdn.jsdelivr.net/npm/katex@{KATEX_VERSION}/dist"
FILES_TO_DOWNLOAD = {
    "katex.min.js": f"{CDN_BASE}/katex.min.js",
    "katex.min.css": f"{CDN_BASE}/katex.min.css",
    "auto-render.min.js": f"{CDN_BASE}/contrib/auto-render.min.js",
    "fonts/KaTeX_AMS-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_AMS-Regular.woff2",
    "fonts/KaTeX_Caligraphic-Bold.woff2": f"{CDN_BASE}/fonts/KaTeX_Caligraphic-Bold.woff2",
    "fonts/KaTeX_Caligraphic-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Caligraphic-Regular.woff2",
    "fonts/KaTeX_Fraktur-Bold.woff2": f"{CDN_BASE}/fonts/KaTeX_Fraktur-Bold.woff2",
    "fonts/KaTeX_Fraktur-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Fraktur-Regular.woff2",
    "fonts/KaTeX_Main-Bold.woff2": f"{CDN_BASE}/fonts/KaTeX_Main-Bold.woff2",
    "fonts/KaTeX_Main-BoldItalic.woff2": f"{CDN_BASE}/fonts/KaTeX_Main-BoldItalic.woff2",
    "fonts/KaTeX_Main-Italic.woff2": f"{CDN_BASE}/fonts/KaTeX_Main-Italic.woff2",
    "fonts/KaTeX_Main-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Main-Regular.woff2",
    "fonts/KaTeX_Math-BoldItalic.woff2": f"{CDN_BASE}/fonts/KaTeX_Math-BoldItalic.woff2",
    "fonts/KaTeX_Math-Italic.woff2": f"{CDN_BASE}/fonts/KaTeX_Math-Italic.woff2",
    "fonts/KaTeX_SansSerif-Bold.woff2": f"{CDN_BASE}/fonts/KaTeX_SansSerif-Bold.woff2",
    "fonts/KaTeX_SansSerif-Italic.woff2": f"{CDN_BASE}/fonts/KaTeX_SansSerif-Italic.woff2",
    "fonts/KaTeX_SansSerif-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_SansSerif-Regular.woff2",
    "fonts/KaTeX_Script-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Script-Regular.woff2",
    "fonts/KaTeX_Size1-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Size1-Regular.woff2",
    "fonts/KaTeX_Size2-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Size2-Regular.woff2",
    "fonts/KaTeX_Size3-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Size3-Regular.woff2",
    "fonts/KaTeX_Size4-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Size4-Regular.woff2",
    "fonts/KaTeX_Typewriter-Regular.woff2": f"{CDN_BASE}/fonts/KaTeX_Typewriter-Regular.woff2",
}

# KaTeX initialization script
KATEX_INIT = """document.addEventListener("DOMContentLoaded", function () {
	renderMathInElement(document.body, {
          delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
          ],
	});
});
"""

# Font families and their variants
KATEX_FONTS = {
    "KaTeX_AMS": ["Regular"],
    "KaTeX_Caligraphic": ["Bold", "Regular"],
    "KaTeX_Fraktur": ["Bold", "Regular"],
    "KaTeX_Main": ["Bold", "BoldItalic", "Italic", "Regular"],
    "KaTeX_Math": ["BoldItalic", "Italic"],
    "KaTeX_SansSerif": ["Bold", "Italic", "Regular"],
    "KaTeX_Script": ["Regular"],
    "KaTeX_Size1": ["Regular"],
    "KaTeX_Size2": ["Regular"],
    "KaTeX_Size3": ["Regular"],
    "KaTeX_Size4": ["Regular"],
    "KaTeX_Typewriter": ["Regular"]
}

def download_file(url: str, dest_path: Path) -> None:
    """Download a file from URL to destination path."""
    response = requests.get(url)
    response.raise_for_status()

    # Create parent directories if they don't exist
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the file
    with open(dest_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {url} to {dest_path}")

def generate_font_face(family: str, variant: str) -> str:
    """Generate a single @font-face declaration."""
    return f"""@font-face {{
    font-family: '{family}';
    src: url('fonts/{family}-{variant}.woff2') format('woff2');
    font-weight: {'bold' if variant == 'Bold' else 'normal'};
    font-style: {'italic' if 'Italic' in variant else 'normal'};
}}"""

def generate_fonts_scss():
    """Generate SCSS file for KaTeX fonts."""
    STYLES_DIR.mkdir(exist_ok=True)

    # Generate all font-face declarations
    font_faces = []
    for family, variants in KATEX_FONTS.items():
        for variant in variants:
            font_faces.append(generate_font_face(family, variant))

    # Write the SCSS file
    scss_content = "\n\n".join(font_faces)
    with open(STYLES_DIR / "_katex_fonts.scss", 'w') as f:
        f.write(scss_content)
    print("Generated _katex_fonts.scss")

def setup_katex():
    """Set up KaTeX files and configuration."""
    print(f"Setting up KaTeX v{KATEX_VERSION}...")

    # Create necessary directories
    STATIC_DIR.mkdir(exist_ok=True)
    FONTS_DIR.mkdir(exist_ok=True)

    # Download all required files
    for file_path, url in FILES_TO_DOWNLOAD.items():
        dest_path = STATIC_DIR / file_path
        download_file(url, dest_path)

    # Rename katex.min.css to katex.css to match existing setup
    css_path = STATIC_DIR / "katex.min.css"
    if css_path.exists():
        css_path.rename(STATIC_DIR / "katex.css")

    # Create katex-init.js
    with open(STATIC_DIR / "katex-init.js", 'w') as f:
        f.write(KATEX_INIT)
    print("Created katex-init.js")

    # Generate fonts SCSS
    generate_fonts_scss()

    print("\nKaTeX setup complete!")
    print("\nRemember to:")
    print("1. Enable KaTeX per page by adding:")
    print("   extra:")
    print("     katex: true")
    print("   to the page's front matter.")
    print("2. Import _katex_fonts.scss in your main SCSS file:")
    print("   @import 'katex_fonts';")

if __name__ == "__main__":
    setup_katex()
