from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Get the User-Agent
        agent = self.headers.get('User-Agent', 'Unknown')
        
        # 2. PRINT IT (This goes to Vercel Logs)
        print(f"!!! MY USER AGENT IS: {agent} !!!")

        # 3. Send a fake playlist so OTT Navigator doesn't show "Error"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"#EXTM3U\n#EXTINF:-1,Test Channel\nhttp://google.com")
        
