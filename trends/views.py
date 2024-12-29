from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient
import requests
import time
from datetime import datetime
import uuid
from django.shortcuts import render
from decouple import config

def index(request):
    return render(request, 'index.html')

proxyMeshUsername = config('PROXY_MESH_USERNAME')
proxyMeshPassword = config('PROXY_MESH_PASSWORD')
twitterUsername = config('TWITTER_USERNAME')
twitterPassword = config('TWITTER_PASSWORD')

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017/')
db = client['twitter_trends']
collection = db['trending_topics']

# Selenium setup
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome()

# ProxyMesh setup
PROXY = f"http://{proxyMeshUsername}:{proxyMeshPassword}@us.proxymesh.com:31280"
options.add_argument(f'--proxy-server={PROXY}')

def get_trending_topics():
    try:
        # Open Twitter
        browser.get('https://x.com/i/flow/login')
        time.sleep(10)
        # Log in
        username_input = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        username_input.send_keys(twitterUsername)
        next_button = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
        next_button.click()
        time.sleep(5)
        password_input = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(twitterPassword)
        submit_button = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        submit_button.click()
        time.sleep(15)
        # Fetch trending topics
        browser.get('https://x.com/explore/tabs/trending')
        trends = browser.find_elements(By.XPATH, ".//span[contains(text(), '#')]")
        top_trends = [trend.text for trend in trends]
        # Store results in MongoDB
        unique_id = str(uuid.uuid4())
        ip_address = requests.get('https://api.ipify.org').text
        timestamp = datetime.now()
        record = {
            "_id": unique_id,
            "trend1": top_trends[0],
            "trend2": top_trends[1],
            "trend3": top_trends[2],
            "trend4": top_trends[3],
            "trend5": top_trends[4],
            "timestamp": timestamp,
            "ip_address": ip_address
        }
        collection.insert_one(record)
        return record

    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    finally:
        browser.quit()

def run_script(request):
    record = get_trending_topics()
    if record:
        return render(request, 'results.html', {"record": record})
    else:
        return render(request, 'results.html', {"error": "Failed to fetch trending topics"})