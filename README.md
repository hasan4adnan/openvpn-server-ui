# 🌐 OpenVPN Server <img width="1203" alt="Ekran Resmi 2025-06-10 18 10 11" src="https://github.com/user-attachments/assets/27dbdace-738b-4cb2-bb8f-232eb9fcc375" />
Web UI<img width="1248" alt="Ekran Resmi 2025-06-10 18 34 16" src="https://github.com/user-attachments/assets/f5566cd1-1de8-460f-90ec-70202c19469f" />

<img width="1721" alt="Ekran Resmi 2025-06-10 18 53 52" src="https://github.com/user-attachments/assets/9d5ef9b8-fdff-495f-bd5b-acb023dafa12" />
<img width="575" alt="Ekran Resmi 2025-06-10 18 28 29" src="https://github.com/user-attachments/assets/3e237f26-b499-478c-aba5-9ef1ac26747f" />

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



