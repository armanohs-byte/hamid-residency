"""
Hamid Residency - Complete Quality, Asset, Map & Static Verification Test
"""
import os
import re
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EXACT_LISTING = "https://www.google.com/maps/place/Hamid+Residency/@26.342763,89.4427175,17z/data=!4m6!3m5!1s0x39e2ff03bf13087d:0x9c86ab54c8563e05!8m2!3d26.342763!4d89.4452924!16s%2Fg%2F11xnq7nx8s"
EXACT_DIRECTIONS = "https://www.google.com/maps/dir/?api=1&destination=26.342763,89.4452924"
EXPECTED_LAT = 26.342763
EXPECTED_LNG = 89.4452924

def check_files_exist():
    print("--- 1. Checking File Integrity ---")
    required_files = [
        "index.html",
        "floor-plans.html",
        "location.html",
        "contact.html",
        "assets/css/style.css",
        "assets/css/responsive.css",
        "assets/js/main.js",
        "assets/js/enquiry.js",
        "assets/data/property-data.json",
        "assets/images/logo.svg",
        "assets/images/exterior-facade.jpg",
        "assets/images/modular-kitchen.jpg",
        "assets/images/modern-bathroom.jpg",
        "assets/images/first-floor-living.jpg",
        "assets/images/bright-bedroom.jpg"
    ]
    all_ok = True
    for f in required_files:
        path = os.path.join(BASE_DIR, f)
        if os.path.exists(path):
            size_kb = os.path.getsize(path) / 1024
            print(f"  [OK] {f} ({size_kb:.1f} KB)")
        else:
            print(f"  [FAIL] Missing file: {f}")
            all_ok = False
    return all_ok

def check_html_links_and_alts():
    print("\n--- 2. Checking HTML Markup, Alt Tags & Internal Links ---")
    html_files = ["index.html", "floor-plans.html", "location.html", "contact.html"]
    issues = []

    for hf in html_files:
        path = os.path.join(BASE_DIR, hf)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        if "<!DOCTYPE html>" not in content:
            issues.append(f"{hf}: Missing <!DOCTYPE html>")
        if "<title>" not in content:
            issues.append(f"{hf}: Missing <title>")

        img_tags = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
        for tag in img_tags:
            if 'alt=' not in tag:
                issues.append(f"{hf}: Image tag without alt attribute: {tag}")

        refs = re.findall(r'(?:href|src)=["\']([^"\'#:]+)["\']', content)
        for ref in refs:
            if ref.startswith("http") or ref.startswith("tel:") or ref.startswith("mailto:") or ref.startswith("//"):
                continue
            ref_path = os.path.normpath(os.path.join(BASE_DIR, ref))
            if not os.path.exists(ref_path):
                issues.append(f"{hf}: Broken internal reference -> {ref}")

    if not issues:
        print("  [OK] All HTML documents have valid DOCTYPE, title, image alt attributes, and zero broken local links.")
        return True
    else:
        for iss in issues:
            print(f"  [FAIL] {iss}")
        return False

def check_maps_and_coordinates():
    print("\n--- 3. Checking Exact Google Maps Pins & Coordinates ---")
    files = ["index.html", "location.html", "contact.html"]
    errors = []

    for hf in files:
        path = os.path.join(BASE_DIR, hf)
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()

        if "26.3350" in html or "89.4625" in html:
            errors.append(f"{hf}: Contains old approximate coordinates!")

        # Verify buttons
        if EXACT_LISTING not in html:
            errors.append(f"{hf}: Missing exact listing link ({EXACT_LISTING})")
        if EXACT_DIRECTIONS not in html:
            errors.append(f"{hf}: Missing exact directions link ({EXACT_DIRECTIONS})")

    # Check Schema.org in index.html
    with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
        idx = f.read()
    schema_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', idx, re.DOTALL)
    if schema_match:
        try:
            s = json.loads(schema_match.group(1))
            lat = s.get("geo", {}).get("latitude")
            lng = s.get("geo", {}).get("longitude")
            if lat != EXPECTED_LAT or lng != EXPECTED_LNG:
                errors.append(f"Schema geo mismatch: {lat}, {lng}")
        except Exception as e:
            errors.append(f"Schema JSON error: {e}")

    if not errors:
        print(f"  [OK] All pages verified with exact coordinates ({EXPECTED_LAT}, {EXPECTED_LNG}) and listing/directions links.")
        return True
    else:
        for err in errors:
            print(f"  [FAIL] {err}")
        return False

if __name__ == "__main__":
    t1 = check_files_exist()
    t2 = check_html_links_and_alts()
    t3 = check_maps_and_coordinates()

    if t1 and t2 and t3:
        print("\n=== ALL AUDIT & INTEGRITY CHECKS PASSED PERFECTLY ===")
        sys.exit(0)
    else:
        print("\n=== SOME CHECKS FAILED ===")
        sys.exit(1)
