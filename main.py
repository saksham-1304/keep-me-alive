#!/usr/bin/env python3
import requests
import datetime
import time

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

def keep_servers_alive():
    """Continuously ping all servers every 5 minutes"""
    print("🚀 Starting Keep Servers Alive script...")
    print(f"Will ping {len(URLS_TO_PING)} servers every 5 minutes")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    
    while True:
        try:
            ping_all_backends()
            
            # Wait for 5 minutes (300 seconds)
            print(f"\n⏰ Waiting 5 minutes before next round...")
            print(f"Next ping scheduled at: {(datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S')}")
            time.sleep(300)  # 5 minutes = 300 seconds
            
        except KeyboardInterrupt:
            print("\n\n🛑 Script stopped by user")
            print("All servers will no longer be kept alive")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error in main loop: {e}")
            print("Waiting 1 minute before retrying...")
            time.sleep(60)

if __name__ == "__main__":
    keep_servers_alive()