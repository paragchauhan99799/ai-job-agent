# Job Scraper Design

The job scraping system collects job listings from online platforms.

Initial sources:

- Indeed
- LinkedIn
- Company career pages

---

# Scraper Framework

Each scraper should inherit from a base scraper class.

Responsibilities:

- fetch job pages
- parse job data
- normalize fields
