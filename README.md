# Twitter Trending Topics Scraper

This project is a Django web application that uses Selenium to scrape the top 5 trending topics from Twitter, stores the results in MongoDB, and displays them on a web page. The project also utilizes ProxyMesh to route requests through rotating IP addresses.

---

## Features
1. **Scrape Twitter Trends**: Logs into Twitter, fetches the top 5 trending topics under the "What's Happening" section, and captures the timestamp and IP address used.
2. **ProxyMesh Integration**: Ensures each request to scrape Twitter is routed through a different IP address.
3. **Data Storage**: Saves the trending topics, timestamp, IP address, and a unique ID for each run in MongoDB.
4. **Django Web Interface**:
   - A home page with a link to trigger the scraping process.
   - A results page displaying the fetched data and a JSON representation.

---

## Prerequisites
### Software Requirements:
- Python 3.7+
- MongoDB
- Google Chrome

### Python Libraries:
- `selenium`
- `django`
- `pymongo`
- `requests`
- `webdriver-manager`
- `decouple`

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Jinesh-Jain1507/Stir-internship-assignment.git
cd twitter-trending-topics-scraper
```

### 2. Install Dependencies
```bash
pip install selenium django pymongo requests webdriver-manager decouple
```

### 3. Start MongoDB
Ensure MongoDB is running locally or update the connection string in `views.py`:
```python
client = MongoClient('mongodb://localhost:27017/')
```

### 4. Configure Twitter Credentials
Update the placeholders in the `.env.sample` file in your `.env` file

### 5. Run the Application
#### a. Start the Django Server:
```bash
python manage.py runserver
```

#### b. Access the Application:
Visit `http://127.0.0.1:8000/` in your browser.

---

## Usage
### Home Page
- Click the link `Click here to run the script` to initiate scraping.

### Results Page
- Displays the top 5 trending topics, timestamp, IP address used, and a JSON extract of the stored record.
- Provides a link to rerun the scraping process.
