import requests
from bs4 import BeautifulSoup
import os


def web_file_scanner():
    target_url = "https://gemini.google.com/"
    if not os.path.exists("my_downloads"):
        os.makedirs("my_downloads")
        print("Downloads folder created")

    print("Connecting to website...")
    response = requests.get(target_url)

    soup = BeautifulSoup(response.text, "html.parser")

    #PART B:
    links = soup.find_all("a")
    print(f"Found {len(links)} links on the website")

    for link in links:
        href = link.get("href")

        if not href:
            continue

        if href.startswith("/"):
            full_url = target_url + href
        elif href.startswith("http"):
            full_url = href
        else:
            full_url = target_url + "/" + href

        print("Checking:", full_url)

        #PART C:
        if full_url.lower().endswith((".pdf", ".jpg")):
            print("File found, downloading...")
            try:
                file_data = requests.get(full_url).content
                file_name = os.path.join("my_downloads", full_url.split("/")[-1])
                with open(file_name, "wb") as file:
                    file.write(file_data)
                print(f"Saved: {file_name}")
            except Exception as e:
                print(f"Failed to download {full_url}: {e}")

    print("\nScan completed successfully.")

web_file_scanner()
