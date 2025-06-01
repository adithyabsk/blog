#!/usr/bin/env -S uv run --script

import tomllib
from pathlib import Path

REDIRECT_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0; URL={redirect_url}">
    <link rel="canonical" href="{redirect_url}">
</head>
<body>
    <p>Redirecting to <a href="{redirect_url}">{redirect_url}</a>...</p>
</body>
</html>"""

def generate_redirects():
    # Load redirect config
    with open("config/_redirects.toml", "rb") as f:
        redirects = tomllib.load(f)["redirects"]
    
    # Create redirect pages
    for old_path, new_path in redirects.items():
        # Remove leading slash but keep the .html extension
        path = old_path.lstrip("/")
        
        # Create directory structure
        redirect_dir = Path("static") / path
        redirect_dir.parent.mkdir(parents=True, exist_ok=True)
        
        # Write redirect file
        with open(redirect_dir, "w") as f:
            f.write(REDIRECT_TEMPLATE.format(redirect_url=new_path))

if __name__ == "__main__":
    generate_redirects()
