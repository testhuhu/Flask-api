from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def fetch_octoplus_news():
    try:
        url = "https://octoplusbox.com/news/"
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        items = soup.select("div.news-archive ul li")[:3]
        return [li.get_text(strip=True) for li in items]
    except Exception as e:
        return [f"خطأ جلب أخبار Octoplus: {e}"]

def fetch_hackernews_top():
    try:
        url = "https://thehackernews.com/"
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        items = soup.select("h2.home-title a")[:2]
        return [a.get_text(strip=True) for a in items]
    except Exception as e:
        return [f"خطأ جلب أخبار أمنية: {e}"]

def fetch_mobile_security():
    try:
        url = "https://portswigger.net/daily-swig/mobile"
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        items = soup.select("h3 a")[:2]
        return [a.get_text(strip=True) for a in items]
    except Exception as e:
        return [f"خطأ جلب أخبار الجوال: {e}"]

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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
