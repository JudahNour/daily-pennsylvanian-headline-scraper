"""
Scrapes a headline from The Daily Pennsylvanian website and saves it to a 
JSON file that tracks headlines over time.
"""

import os
import sys

import daily_event_monitor

import bs4
import requests
import loguru
    
def scrape_data_point():
    """
    Scrapes the title of the latest crossword from The Daily Pennsylvanian Crosswords page.

    Returns:
        str: The crossword title if found, otherwise an empty string.
    """
    # URL of the Crosswords page
    crossword_page_url = "https://www.thedp.com/section/crosswords"
    req = requests.get(crossword_page_url)
    loguru.logger.info(f"Request URL (Crosswords page): {req.url}")
    loguru.logger.info(f"Request status code (Crosswords page): {req.status_code}")

    latest_crossword_title = ""
    if req.ok:
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        # Find the latest crossword article
        latest_article = soup.find("div", class_="row section-article")
        if latest_article:
            title_element = latest_article.find("h3", class_="standard-link")
            if title_element and title_element.a:
                latest_crossword_title = title_element.a.text.strip()
                loguru.logger.info(f"Latest crossword title: {latest_crossword_title}")

    return latest_crossword_title




if __name__ == "__main__":

    # Setup logger to track runtime
    loguru.logger.add("scrape.log", rotation="1 day")

    # Create data dir if needed
    loguru.logger.info("Creating data directory if it does not exist")
    try:
        os.makedirs("data", exist_ok=True)
    except Exception as e:
        loguru.logger.error(f"Failed to create data directory: {e}")
        sys.exit(1)

    # Load daily event monitor
    loguru.logger.info("Loading daily event monitor")
    dem = daily_event_monitor.DailyEventMonitor(
        "data/daily_pennsylvanian_headlines.json"
    )

    # Run scrape
    loguru.logger.info("Starting scrape")
    try:
        data_point = scrape_data_point()
    except Exception as e:
        loguru.logger.error(f"Failed to scrape data point: {e}")
        data_point = None

    # Save data
    if data_point is not None:
        dem.add_today(data_point)
        dem.save()
        loguru.logger.info("Saved daily event monitor")

    def print_tree(directory, ignore_dirs=[".git", "__pycache__"]):
        loguru.logger.info(f"Printing tree of files/dirs at {directory}")
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in ignore_dirs]
            level = root.replace(directory, "").count(os.sep)
            indent = " " * 4 * (level)
            loguru.logger.info(f"{indent}+--{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for file in files:
                loguru.logger.info(f"{sub_indent}+--{file}")

    print_tree(os.getcwd())

    loguru.logger.info("Printing contents of data file {}".format(dem.file_path))
    with open(dem.file_path, "r") as f:
        loguru.logger.info(f.read())

    # Finish
    loguru.logger.info("Scrape complete")
    loguru.logger.info("Exiting")
