import requests
from bs4 import BeautifulSoup
from datetime import datetime
from storage import save_news_to_firebase

def scrape_esana_news():
    BASE_URL = 'https://esana.com.lk/'  # Define the base URL
    URL = f'{BASE_URL}/news'  # Construct the full news URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage. Error: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    news_items = []

    # Adjust the class names and HTML structure based on the website's actual HTML
    articles = soup.find_all('div', class_='col-lg-6')

    for article in articles:
        img_tag = article.find('img')
        imgLink = img_tag['src'] if img_tag else "No image"

        title_tag = article.find('h3').find('a')
        title = title_tag.text.strip() if title_tag else "No title"
        relative_link = title_tag['href'] if title_tag else "No link"
        link = f'{BASE_URL}{relative_link}'  # Construct the full link

        date_tag = article.find('ul', class_='list-inline').find('a')
        time = date_tag.text.strip() if date_tag else "No date"

        # Scrape news details for post content
        news_details = scrapeNewsDetails(link)

        # Create a dictionary for the news item
        news_items.append({
            'id': relative_link.split('/')[-1],  # Assuming the ID is the last part of the link
            'title': title,
            'link': link,
            'imgLink': imgLink,
            'date': datetime.now().isoformat(),
            'time': time,
            'agency': 'esana',
            'agencyLogoLink': 'https://esana.com.lk/assets/img/esena-logo.webp',
            'postContent': news_details['post_content']
        })

    # Send data to Firebase
    save_news_to_firebase(news_items)

def scrapeNewsDetails(url):
    print(f"Scraping news details from: {url}")
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract details
    headline = soup.find('h2', class_='m-t-xs-20 m-b-xs-0 axil-post-title hover-line').text.strip()
    posted_time = soup.find('div', class_='post-metas banner-post-metas m-t-xs-20').text.strip()
    image_link = soup.find('img', class_='img-fluid')['src']

    # Extract the post content
    content_div = soup.find('div', class_='single-blog-wrapper')
    if content_div:
        paragraphs = content_div.find_all('p')
        full_content = ' '.join(p.get_text(separator=' ') for p in paragraphs)

        # Split the content into two halves and take the first half
        post_content = full_content[len(full_content) // 2:]
    else:
        post_content = 'Content not available'
    return {
        'headline': headline,
        'posted_time': posted_time,
        'image_link': image_link,
        'post_content': post_content
    }

