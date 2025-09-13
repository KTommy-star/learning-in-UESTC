#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的HTTP服务器，用于在本地网络中分享网页
使用方法：
1. 确保已安装Python 3
2. 在命令行中运行：python server.py
3. 在浏览器中访问显示的地址
"""

import http.server
import socketserver
import socket
import webbrowser
import os
import sys

def get_local_ip():
    """获取本机IP地址"""
    try:
        # 连接到一个远程地址来获取本地IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def start_server(port=8000):
    """启动HTTP服务器"""
    # 切换到脚本所在目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # 创建服务器
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            local_ip = get_local_ip()
            
            print("="*60)
            print("🎉 网页服务器已启动！")
            print("="*60)
            print(f"📱 本机访问地址: http://localhost:{port}")
            print(f"🌐 局域网访问地址: http://{local_ip}:{port}")
            print("="*60)
            print("📋 其他设备访问步骤：")
            print("1. 确保所有设备连接到同一个WiFi网络")
            print(f"2. 在其他设备的浏览器中输入: http://{local_ip}:{port}")
            print("3. 打开index.html文件")
            print("="*60)
            print("⚠️  注意事项：")
            print("- 请确保防火墙允许此端口的连接")
            print("- 如果无法访问，请检查网络设置")
            print("- 按 Ctrl+C 停止服务器")
            print("="*60)
            
            # 自动打开浏览器
            try:
                webbrowser.open(f"http://localhost:{port}")
            except:
                pass
            
            print("🚀 服务器运行中...")
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 98 or e.errno == 10048:  # 端口被占用
            print(f"❌ 端口 {port} 已被占用，尝试使用端口 {port + 1}")
            start_server(port + 1)
        else:
            print(f"❌ 启动服务器失败: {e}")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
        sys.exit(0)

if __name__ == "__main__":
    start_server()