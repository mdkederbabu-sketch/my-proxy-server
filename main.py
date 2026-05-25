import os
from flask import Flask, request
import requests

app = Flask(__name__)

# তোমার দেওয়া Evomi প্রক্সি ডিটেইলস (Username:Password Auth সহ)
PROXY_URL = "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-california_hardsession-RLX8SS2QV@core-residential.evomi.com:1002"

@app.route('/')
def home():
    # ইউজার যে লিঙ্ক ভিজিট করতে চায়, ডিফল্ট হিসেবে আইপি চেকার দেওয়া
    target_url = request.args.get('url', 'https://api.ipify.org?format=json')
    
    proxies = {
        "http": PROXY_URL,
        "https": PROXY_URL,
    }
    
    try:
        # রিকোয়েস্টটি সরাসরি প্রক্সি দিয়ে পাঠানো হচ্ছে
        response = requests.get(target_url, proxies=proxies, timeout=15)
        return response.text
    except Exception as e:
        return f"Proxy Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
