# Python Web File Scanner & Downloader

A functional Python script designed for automated web reconnaissance and file harvesting. 

## Features
* Connects to a target URL and parses HTML structure.
* Extracts and correctly handles both absolute and relative hyperlinks.
* Filters discovered links for specific extensions (`.pdf`, `.jpg`).
* Automatically creates a local folder and downloads the targeted files.
* Includes exception handling for network requests to ensure stability.

## Prerequisites & Libraries
The script runs on Python 3 and uses the following built-ins and external libraries:
* `requests`
* `beautifulsoup4`
* `os`

## How It Works
1. The script initializes and ensures a local download folder exists.
2. It sends an HTTP GET request to the target website.
3. It extracts all `<a>` anchor tags and reconstructs full URLs.
4. If a file matches the target extensions, it downloads and saves it locally.
