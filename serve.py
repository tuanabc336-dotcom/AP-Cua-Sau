"""Máy chủ tĩnh nhỏ cho Bé Vui Học.

Chạy: python serve.py 8123
Mở:   http://127.0.0.1:8123

Luôn gửi header no-store để trình duyệt không dùng lại CSS/JS cũ
trong lúc chỉnh sửa nội dung. Lắng nghe trên mọi giao diện mạng (0.0.0.0)
để điện thoại cùng Wi-Fi cũng truy cập được.
"""

import functools
import http.server
import os
import socket
import socketserver
import sys


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8123
    root = os.path.dirname(os.path.abspath(__file__))
    handler = functools.partial(Handler, directory=root)
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("0.0.0.0", port), handler) as httpd:
        httpd.daemon_threads = True
        print("Serving Be Vui Hoc at http://127.0.0.1:%d" % port)
        print("Tren dien thoai (cung Wi-Fi): http://%s:%d" % (lan_ip(), port))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
