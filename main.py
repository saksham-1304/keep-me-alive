#!/usr/bin/env python3
import requests
import datetime

# List of URLs to keep alive - replace these with your actual server URLs
URLS_TO_PING = [
    "https://askmypdf-ai-powered-pdf-chat.onrender.com",
    "https://refactora-ai.onrender.com", 
    "https://vibeconnect-k1te.onrender.com/",
    "https://echobrain-ai-powered-second-brain.onrender.com/"
]

def ping_backend(url):
    try:
        print(f"{datetime.datetime.now()}: Pinging {url}")
        response = requests.get(url, timeout=30)
        print(f"Response: {response.status_code}")
        
        if response.status_code == 200:
            print(f"✅ {url} is alive")
        else:
            print(f"⚠️ {url} returned unexpected status code: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error pinging {url}: {e}")

def ping_all_backends():
    print(f"Starting to ping {len(URLS_TO_PING)} servers...")
    print("=" * 50)
    
    for i, url in enumerate(URLS_TO_PING, 1):
        print(f"\n[{i}/{len(URLS_TO_PING)}] Checking server:")
        ping_backend(url)
    
    print("\n" + "=" * 50)
    print("Finished pinging all servers")

if __name__ == "__main__":
    ping_all_backends()