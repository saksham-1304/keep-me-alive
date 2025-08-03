### Keep your servers alive for free

Traditionally if you use renders free plan, they shut down your server after 15 minutes of inactivity. With this repo, you can keep multiple servers alive constantly by pinging them every 5 minutes!

**Features:**
- Support for multiple server URLs (up to 5 configured by default)
- Individual status tracking for each server
- Detailed logging with timestamps
- Error handling for each server independently

Steps:
1. Clone the repo
2. In main.py, update the `URLS_TO_PING` list with your respective server URLs & endpoints:
   ```python
   URLS_TO_PING = [
       "https://your-server-1.org/ping",
       "https://your-server-2.org/ping", 
       "https://your-server-3.org/ping",
       "https://your-server-4.org/ping",
       "https://your-server-5.org/ping"
   ]
   ```
3. Create your own github repo and navigate to the actions tab, which is located between your pull requests and projects.
4. On the actions tab, you should see something called 'Keep Backend Alive', click on it and click Run Workflow
5. You're all set!

   Note that github actions isn't always 100% accurate, there are times where instead of pinging every 5 minutes like we want it to, it may ping it with a delay (5-10 minutes) when servers are busy.

**Tips:**
- You can add or remove URLs from the `URLS_TO_PING` list as needed
- Each server is pinged independently, so if one fails, others will still be checked
- The script provides clear status indicators (✅ for success, ❌ for errors, ⚠️ for unexpected responses)
   
