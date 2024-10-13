import schedule
from crawler import scrape_esana_news
from storage import delete_news_collection

def job():
    print("Starting the news scraping process...")
    scrape_esana_news()
    print("News scraping process completed.")

def delete_job():
    print("Deleting the news collection...")
    delete_news_collection()
    print("News collection deletion completed.")

# Schedule the job to run every 5 minutes
schedule.every(5).minutes.do(job)
# Schedule the delete_job to run every 48 hours
schedule.every(36).hours.do(delete_job)

def run_pending():
    schedule.run_pending()
