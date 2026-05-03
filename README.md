<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C2FF,25:00F5FF,50:7F00FF,75:FF00F5,100:00C2FF&height=180&section=header&text=SentinalVaultX&fontSize=40&fontColor=ffffff&animation=fadeIn" />
</p>

# 🔐 SentinalVaultX – AI Security & Intrusion Detection System

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=600&lines=AI+Powered+Security+System;Real-time+Intrusion+Detection;Smart+Face+Recognition+Engine" />

<br/>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![AI](https://img.shields.io/badge/AI-Facial_Recognition-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)

</div>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=3" />
</p>

<br/>

<p align="center">
🚀 A smart AI-based security system that detects unauthorized access using facial recognition and provides real-time alerts via a web dashboard.
</p>

<br/>
---
## 📸 Preview

<img width="1920" height="1080" alt="0a21fb75ebf3f07d3afef12db6523043949a23e9a3f02e70ccf26148e99e0f19" src="https://github.com/user-attachments/assets/a22cc5ee-391b-426e-ad53-76707df3a1b7" />

<img width="1920" height="1080" alt="0d98a51a2e57c7bb8904a68e9f62da37bf0bdb2aa3d094ef5b98770b3dde0bd3" src="https://github.com/user-attachments/assets/16d6ccf2-51af-4260-9da7-7804ec252880" />

<img width="1920" height="1080" alt="67618c9fd24200465e9f0f71ab3e718af23af106c3b441e37f2ce169c6ba3c3d" src="https://github.com/user-attachments/assets/a0ddbb5e-e53d-421f-a6ea-374e95ae4c8c" />


---

## ✨ *Key Features*

### 🧠 AI-Based Intrusion Detection

* 🔍 Face recognition using deep learning
* 🚫 Detects unauthorized users in real-time
* 🎯 Smart classification of authorized vs intruders

### 🌐 Web-Based Control Panel

* 📊 Live dashboard with system status
* 🧑‍💻 Admin control for approvals & bans
* 📱 Accessible from laptop, phone, or any device

### ⚡ Real-Time Alerts

* 📡 Instant alert system for intrusions
* 📧 Email notifications
* 📲 SMS alerts (integration ready)

### 🎨 Modern UI/UX

* 🌙 Dark mode support
* ⚡ Live WebSocket updates
* 📱 Responsive design

---

## 🛠 *Tech Stack*

| Component   | Technology                 |
| ----------- | -------------------------- |
| 🐍 Backend  | Python, Flask              |
| 🧠 AI Model | InsightFace, OpenCV        |
| 🌐 Frontend | HTML, CSS, JavaScript      |
| ⚡ Real-Time | Flask-SocketIO             |
| 💾 Database | SQLite                     |
| 📡 Alerts   | SMTP (Email), Twilio-ready |

---

## 📦 *Project Architecture*

```
SentinalVaultX/
│
├── app.py                  # Flask web server
├── face_detection.py       # Face recognition engine
├── notification_service.py # Alert & notification logic
├── preprocess.py
├── create_embeddings.py
│
├── templates/
├── static/
│
├── requirements.txt
└── README.md
```

---

## 🔄 *System Flow*

1. 📷 Camera captures user face
2. 🧠 Face embeddings are generated
3. 🔍 System compares with stored embeddings
4. 🚨 Unauthorized access triggers alert
5. 🌐 Dashboard updates in real-time
6. 👤 Admin reviews and approves/bans user

---

## ⚙ *Setup Guide*

### 1. Clone Repository

```bash
git clone https://github.com/Shaurya-2004/SentinalVaultX.git
cd SentinalVaultX
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create `.env` file:

```env
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-password
TWILIO_ACCOUNT_SID=your-sid
TWILIO_AUTH_TOKEN=your-token
TWILIO_PHONE_NUMBER=your-number
SECRET_KEY=your-secret
```

### 4. Run Application

```bash
python app.py
```

### 5. Start Detection Engine

```bash
python face_detection.py
```

---

## 🧪 *How to Test*

1. Start the web application
2. Run the detection script
3. Show an unknown face to camera
4. Check dashboard for alert
5. Approve or ban user from UI

---

## 🎯 *Use Cases*

* 🏦 ATM Security Systems
* 🏠 Home Surveillance
* 🏢 Office Entry Monitoring
* 💻 Personal Device Security (Laptop/PC)

---

## 🧩 *Challenges Faced*

* Handling real-time face recognition performance
* Reducing false positives in detection
* Integrating WebSocket-based live updates
* Secure handling of API credentials

---

## 🔮 *Future Improvements*

* 🛡️ Anti-Spoofing Detection (liveness checks to prevent photo/video attacks)
* 🧠 Advanced anomaly detection using behavioral patterns
* 🌐 Cloud deployment with scalable infrastructure
* 📱 Mobile app integration for remote monitoring
* 🔐 Multi-factor authentication (Face + OTP / PIN)
* 🎥 Continuous video stream analysis instead of frame-based detection
* 📊 Analytics dashboard for intrusion trends and insights

---

## ⚠️ *Disclaimer*

This project is built for educational purposes and should not be used as a production-grade security system without further enhancements.

---

## ⭐ *Show Your Support*

If you found this project interesting, consider giving it a ⭐

---

*Built with 💻 + ☕ + persistence*
