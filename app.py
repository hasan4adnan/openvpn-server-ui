from flask import Flask, request, send_from_directory
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/start', methods=['POST'])
def start_vpn():
    try:
        result = subprocess.run(['sudo', 'systemctl', 'start', 'openvpn@server'], capture_output=True, text=True)
        return f"✅ VPN started.\n\n{result.stdout}{result.stderr}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

@app.route('/stop', methods=['POST'])
def stop_vpn():
    try:
        result = subprocess.run(['sudo', 'systemctl', 'stop', 'openvpn@server'], capture_output=True, text=True)
        return f"🛑 VPN stopped.\n\n{result.stdout}{result.stderr}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

@app.route('/status', methods=['GET'])
def status_vpn():
    try:
        result = subprocess.run(['sudo', 'systemctl', 'status', 'openvpn@server'], capture_output=True, text=True)
        return f"📋 VPN status:\n\n{result.stdout}{result.stderr}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


