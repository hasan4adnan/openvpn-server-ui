# 🌐 OpenVPN Server Web UI

A lightweight web interface to manage an OpenVPN server hosted on an AWS EC2 instance.

> ✅ Built with Flask + HTML/CSS/JS  
> 🛡️ Designed for self-hosted VPN setups  
> 🔒 Fully functional with Tunnelblick/OpenVPN clients  
> 🚀 Deployed on a t2.micro (Free Tier) instance

---

## 🔧 Features

- ✅ Start/Stop OpenVPN server via web interface  
- 🔍 View OpenVPN service status  
- 🎨 Custom responsive frontend (HTML/CSS/JS)  
- 💻 Hosted securely on your EC2 instance  
- 👤 Client `.ovpn` generation & download supported (via [angristan/openvpn-install](https://github.com/angristan/openvpn-install))

---

## 🛠️ Technologies Used

- **Python 3**  
- **Flask**  
- **OpenVPN**  
- **HTML / CSS / JavaScript**

---

## 📁 Project Structure

vpn-server-ui/
├── app.py # Flask backend to control VPN
├── index.html # Frontend UI (single file)
├── openvpn-install.sh # Angristan's OpenVPN setup script
├── .gitignore # To prevent secret files from being tracked


---

## 🚀 Getting Started

> 🧠 Assumes you already have OpenVPN installed via [angristan/openvpn-install](https://github.com/angristan/openvpn-install)

1. **Connect to your EC2 instance:**

```bash
ssh -i your-key.pem ubuntu@your-public-ip

## Clone the repository:

git clone https://github.com/hasan4adnan/openvpn-server-ui.git
cd openvpn-server-ui

git clone https://github.com/hasan4adnan/openvpn-server-ui.git
cd openvpn-server-ui

## Install Python dependencies:

sudo apt update && sudo apt install python3-pip -y
pip3 install flask
Run the Flask server:
sudo python3 app.py
Visit the web interface:
http://your-public-ip:5000

📦 Security Notes
Sensitive files like .ovpn, .pem, .crt, and .key are ignored via .gitignore
Only the UI logic and control scripts are exposed publicly


🧠 Credits
angristan/openvpn-install – base OpenVPN setup
Flask – lightweight backend framework


📸 Screenshots
Coming soon! (feel free to add Tunnelblick + web UI screenshots)


✍️ Author
Hasan Adnan – @hasan4adnan


🪄 License
MIT License



