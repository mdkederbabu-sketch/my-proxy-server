import os
import concurrent.futures
from flask import Flask, request
import requests

app = Flask(__name__)

# তোমার দেওয়া বিভিন্ন স্টেটের ১২টি প্রক্সি লিস্ট
PROXY_LIST = [
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-california_hardsession-RLX8SS2QV@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-kentucky_hardsession-LY5PP75HS@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-michigan_hardsession-78AI2OICD@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-wisconsin_hardsession-SCY5HJ910@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-tennessee_hardsession-2AZWGOTM0@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-arizona_hardsession-66HDGKQJG@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-maryland_hardsession-GM0WPRSV9@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-colorado_hardsession-A3XPU10B8@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-oklahoma_hardsession-S9ZZKD1YC@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-alabama_hardsession-13YBT4IYM@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-pennsylvania_hardsession-GXN3H7WUU@core-residential.evomi.com:1002",
    "http://realxyroo1:S7WN3AwPReD5kzgYgvma_region-indiana_hardsession-QT1U1CXAX@core-residential.evomi.com:1002"
]

def fetch_ip(proxy_url):
    proxies = {"http": proxy_url, "https": proxy_url}
    try:
        # প্রতিটা প্রক্সি দিয়ে আইপি চেক করার রিকোয়েস্ট
        response = requests.get('https://api.ipify.org?format=json', proxies=proxies, timeout=8)
        if response.status_code == 200:
            return response.json().get('ip', 'Unknown IP')
    except:
        return "Proxy Connection Failed"
    return "Proxy Connection Failed"

@app.route('/')
def home():
    results = []
    
    # একসাথে দ্রুত ১২টি প্রক্সি চেক করার জন্য ThreadPool 
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = [executor.submit(fetch_ip, proxy) for proxy in PROXY_LIST]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
            
    # ১২টি আইপি আলাদা আলাদা লাইনে ব্রাউজারে শো করবে
    return "<br>".join(results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
