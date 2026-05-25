import random
import string
from flask import Flask, Response

app = Flask(__name__)

# ৫ অক্ষরের ইউনিক সেশন আইডি তৈরির ফাংশন
def generate_random_session():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(5))

@app.route('/')
def index():
    # আমেরিকার ১২টি বড় বড় স্টেট ও সিটির লিস্ট (যেন প্রতি লাইনে আলাদা সিটি আসে)
    usa_regions = [
        "california", "new.york", "texas", "florida", "illinois", 
        "pennsylvania", "ohio", "georgia", "north.carolina", "michigan",
        "new.jersey", "virginia"
    ]
    
    # আপনার অ্যাকাউন্ট ক্রেডেনশিয়ালস
    base_format = "core-residential.evomi.com:1002:realxyroo1:S7WN3AwPReD5kzgYgvma"
    
    usa_random_proxies = []
    
    # লুপ চালিয়ে ১২টি ভিন্ন সিটির প্রক্সি তৈরি করা হচ্ছে
    for region in usa_regions:
        random_session = generate_random_session()
        
        # হুবহু আপনার দেখানো ফরম্যাট: base_format + _region-সিটি + _hardsession-কোড
        proxy_line = f"{base_format}_region-{region}_hardsession-{random_session}"
        usa_random_proxies.append(proxy_line)
        
    # ১২টি প্রক্সি এলোমেলো (Shuffle) করে দেওয়া হচ্ছে যেন প্রতি রিফ্রেশে সিকোয়েন্স আলাদা হয়
    random.shuffle(usa_random_proxies)
    
    return Response("\n".join(usa_random_proxies), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
