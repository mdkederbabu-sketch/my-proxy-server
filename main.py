import random
import string
from flask import Flask, Response

app = Flask(__name__)

# এই ফাংশনটি প্রতি লাইনের জন্য একটি ইউনিক ৫ অক্ষরের সেশন আইডি তৈরি করবে
def generate_random_session():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(5))

@app.route('/')
def index():
    # ১. আপনার মূল এভোমি অ্যাকাউন্ট ক্রেডেনশিয়ালস
    host_port = "core-residential.evomi.com:1002"
    base_user = "realxyroo1"
    password = "S7WN3AwPReD5kzgYgvma"
    
    usa_random_proxies = []
    
    # ২. লুপ চালিয়ে ১২টি একদম ভিন্ন ভিন্ন সেশনের (ভিন্ন সিটির) প্রক্সি জেনারেট করা হচ্ছে
    for _ in range(12):
        random_session = generate_random_session()
        
        # এখানে '_region-united.states_' ব্যবহার করায় এভোমি নিজে থেকে আমেরিকার যেকোনো র‍্যান্ডম সিটি সিলেক্ট করবে
        # আর প্রতি লাইনে সেশন আইডি আলাদা হওয়ায় ১২টি আইপিই ১২টি আলাদা সিটির হবে
        proxy_line = f"{host_port}:{base_user}_region-united.states_hardsession-{random_session}:{password}"
        usa_random_proxies.append(proxy_line)
    
    # ৩. স্ক্রিনে ১২টি আইপি একসাথে লিস্ট আকারে দেখাবে
    return Response("\n".join(usa_random_proxies), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
