
# 📰 News Scraper Project

## Overview
This project is a web scraping application designed to fetch news articles from the news website and save them to Firebase. The application deletes existing news collections every 36 hours and scrapes new articles on a scheduled basis. This project is developed for educational purposes to practice web scraping techniques.

## Features
- **Web Scraping:** Retrieves news articles from the Esana website.
- **Firebase Integration:** Saves scraped news articles to Firebase Realtime Database.
- **Scheduled Tasks:** Deletes old news collections every 36 hours and scrapes news articles every 5 minutes.
- **Error Handling:** Handles HTTP requests errors and provides appropriate error messages.
- 
## Technologies Used
- 🐍 Python
- 🌐 BeautifulSoup
- 📦 Requests
- 🔥 Firebase Admin SDK
- ⏰ Schedule


## Installation

1. Clone this repository:

```bash
git clone https://github.com/CharakaMihiranga/NewsScraper.git
cd NewsScraper
```

2. Install the required packages:

```bash
pip install requests beautifulsoup4 firebase-admin schedule
```

3. Set up Firebase:

- Create a Firebase project and configure the Realtime Database.
- Download the serviceAccountKey.json file and place it in the `config` directory.

## Disclaimer

This project is developed for practice in web scraping for educational purposes only. Please ensure that you have permission to scrape any website you target. ⚠️

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 📄
