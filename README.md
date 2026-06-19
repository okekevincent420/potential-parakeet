# Python Job Listings Scraper

A Python web scraper that extracts structured job listing data from a target site 
and exports it to CSV for further analysis or filtering.

---

## Problem Statement

Manually browsing job boards to collect and compare listings is time-consuming. 
This scraper automates the collection of job data — title, company, location, and 
detail page URL — into a clean, structured format ready for analysis or bulk review.

---

## Tech Stack

- **Python** — core language
- **Requests** — HTTP requests to fetch page content
- **Beautiful Soup (bs4)** — HTML parsing and data extraction
- **Pandas** — data manipulation and export
- **CSV module** — output formatting

---

## How It Works

1. Sends an HTTP GET request to the target jobs page
2. Parses the HTML response using Beautiful Soup
3. Extracts job title, company name, location, and detail page URL for each listing
4. Stores all results in a structured CSV file

---

## Output

A CSV file containing one row per job listing:

| Job Title | Company | Location | URL |
|-----------|---------|----------|-----|
| ... | ... | ... | ... |

---

## How to Run

```bash
git clone <your-repo-url>
cd job-listings-scraper
pip install -r requirements.txt
python scraper.py
```

---

## What I'd Improve Next

- Extend to scrape real job boards (LinkedIn, Indeed) with pagination support
- Add filtering by keyword, location, or job type
- Schedule automated runs with `cron` or GitHub Actions
- Store results in a database instead of CSV for easier querying
- Add duplicate detection across runs

---

*Project inspired by [roadmap.sh](https://roadmap.sh/projects/job-listings-scraper)*

