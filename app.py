from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(android)

def fetch_octoplus_news():
    url = "https://octoplusbox.com/news/"
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = soup.select("div.news-archive ul li")[:3]
    return [li.get_text(strip=True) for li in items]

def fetch_hackernews_top():
    url = "https://thehackernews.com/"
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = soup.select("h2.home-title a")[:2]
    return [a.get_text(strip=True) for a in items]

def fetch_mobile_security():
    url = "https://portswigger.net/daily-swig/mobile"
    resp = requests.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    items = soup.select("h3 a")[:2]
    return [a.get_text(strip=True) for a in items]

@app.route("/news", methods=["GET"])
def get_news():
    today = datetime.now().strftime("%Y-%m-%d")
    data = {
        "date": today,
        "octoplus": fetch_octoplus_news(),
        "hackernews": fetch_hackernews_top(),
        "mobilesec": fetch_mobile_security()
    }
    return jsonify(data)

if name == "main":

    app.run(debug=True, host="0.0.0.0")
