import ddddocr

from http.server import BaseHTTPRequestHandler, HTTPServer

class IntegerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应状态码
        self.send_response(200)
        
        # 设置响应头
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        det = ddddocr.DdddOcr(det=False, ocr=False)
    
        with open('target.png', 'rb') as f:
            target_bytes = f.read()
            
        with open('background.jpg', 'rb') as f:
            background_bytes = f.read()
            res = det.slide_match(target_bytes, background_bytes)
            print(res)


        response = f"{{\"x\":{res['target'][0] - res['target_x']}}}"
        
        self.wfile.write(response.encode('utf-8'))

def run_server(server_class=HTTPServer, handler_class=IntegerHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'服务器运行在端口 {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()