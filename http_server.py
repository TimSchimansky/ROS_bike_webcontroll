#!/usr/bin/env python

import http.server
import socketserver
import rospy
import os

PORT = 8000

def serve_site(html_path):

    os.chdir(html_path)
    print("changed directory")

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

if __name__=="__main__":
    # Get parameter from launch file and pass to serve_site()
    serve_site(rospy.get_param('http_server/html_file'))
