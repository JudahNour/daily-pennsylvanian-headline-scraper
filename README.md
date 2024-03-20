# daily-pennsylvanian-headline-scraper

This repository is a simple scraper intended to scrape data from the daily pennsylvanian. 
This was done for Homework 2 of CIS 3500 at Penn

## Changes Made

We've updated our web scraping script to enhance its functionality and adapt to a new use case. Originally, the scraper was designed to fetch the main headline from The Daily Pennsylvanian home page. The modification shifts the focus to the "Crosswords" section, specifically aiming to retrieve the title of the latest crossword puzzle. Below, we outline the changes made and explain the rationale behind these adjustments.

The scraper's target has been changed from the main headline to the latest entry in the "Crosswords" section. This was done to align with the new objective of providing users with the most recent crossword puzzle information.

Instead of fetching an \<a> tag with a specific class from the homepage, the updated scraper first locates the most recent crossword article by finding a div with the class row section-article. This change was necessary as the structure of the crossword page organizes articles within these div elements, differing from the homepage structure.

After identifying the latest crossword entry, the script now looks for an \<h3> tag with the class standard-link within this entry to find the title of the crossword. The assumption here is that the latest crossword's title is encapsulated within this specific tag, following the website's consistent layout for article titles.

The decision to focus on the "Crosswords" section stemmed from a desire to provide users with culturally engaging content that is updated regularly. The methodological adjustments, such as targeting specific HTML elements and adding safety checks, were made to ensure the scraper remains robust against web page structural changes and provides accurate data.
