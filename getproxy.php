<?php
// Evomi থেকে পাওয়া প্রক্সি গেটওয়ে এবং পোর্ট এখানে বসাও
$proxy = 'gw.evomi.com:8000'; // উদাহরণ হিসেবে ৮০০০ দেওয়া, তোমার পোর্ট বসাবে

// ইউজার যে ইউআরএলটি ভিজিট করতে চায় (ডিফল্ট হিসেবে গুগল দেওয়া)
$url = isset($_GET['url']) ? $_GET['url'] : 'https://api.ipify.org?format=json';

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_PROXY, $proxy);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);

$response = curl_exec($ch);

if(curl_errno($ch)){
    echo 'Proxy Error: ' . curl_error($ch);
} else {
    echo $response;
}

curl_close($ch);
?>
