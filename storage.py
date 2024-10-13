import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate('config/serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://se10login-default-rtdb.firebaseio.com/'
})

def save_news_to_firebase(news_items):
    for item in news_items:
        news_ref = db.reference(f'news/{item["id"]}')
        news_ref.set({
            'title': item['title'],
            'link': item['link'],
            'imgLink': item['imgLink'],
            'date': item['date'],
            'time': item['time'],
            'agency': item['agency'],
            'agencyLogoLink': item['agencyLogoLink'],
            'postContent': item['postContent'],
        })
    print("News items saved to Firebase.")
