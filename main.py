import os
from flask import Flask, request
import requests

app = Flask(__name__)

# Evomi থেকে পাওয়া প্রক্সি গেটওয়ে এবং পোর্ট এখানে বসাবে
PROXY_URL = "http://gw.evomi.com:8000"  # তোমার পোর্ট বসাবে

@app.route('/')
def home():
    # ইউজার যে লিঙ্ক ভিজিট করতে চায়, ডিফল্ট হিসেবে আইপি চেকার দেওয়া
    target_url = request.args.get('url', 'https://api.ipify.org?format=json')
    
    proxies = {
        "http": PROXY_URL,
        "https": PROXY_URL,
    }
    
    try:
        response = requests.get(target_url, proxies=proxies, timeout=10)
        return response.text
    except Exception as e:
        return f"Proxy Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
