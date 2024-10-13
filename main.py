import time
from scheduler import run_pending
from storage import delete_news_collection
from crawler import scrape_esana_news

def main():
    # Delete the news collection at startup
    print("Deleting the news collection...")
    delete_news_collection()
    print("News collection deletion completed.")

    # Scrape news once after deletion
    print("Starting the news scraping process...")
    scrape_esana_news()
    print("News scraping process completed.")

    # Schedule for further scraping and deletion
    while True:
        run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()