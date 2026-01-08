from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Capture the User-Agent
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        # 2. Print it to Vercel Logs (for you to see in Dashboard)
        print(f"--- CAPTURED USER AGENT: {user_agent} ---")

        # 3. Display it on your TV Screen (Clever Trick!)
        # We create a fake M3U where the channel name IS the User-Agent.
        m3u_content = f"""#EXTM3U
#EXTINF:-1 group-title="Debug",YOUR ID IS BELOW
http://0.0.0.0/
#EXTINF:-1 group-title="Debug",{user_agent}
http://0.0.0.0/
"""

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(m3u_content.encode('utf-8'))
      
