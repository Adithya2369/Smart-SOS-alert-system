# 🚨 Smart SOS Alert System

A cross-platform emergency alert system built using Python that sends real-time SOS notifications with location details via Email and SMS.

Designed for:
- Raspberry Pi deployment
- Laptop testing
- Wearable/assistive emergency systems
- Safety and emergency response applications

---

# 🎓 Academic Project Information

This repository is a part of my B.Tech Final Year Project and represents **Module 7 of 7** of the complete system.

The project focuses on developing a real-time emergency response and assistive safety system using embedded systems, GPS technologies, communication APIs, and Raspberry Pi-based deployment.

---

# 📌 Features

✅ Real-time SOS triggering  
✅ Email alerts using Gmail SMTP  
✅ SMS alerts using Twilio HTTP API  
✅ Google Maps location sharing  
✅ Laptop testing mode  
✅ Raspberry Pi + USB GPS support  
✅ Lightweight and modular design  
✅ No heavy SDK dependencies  

---

# 🧠 System Overview

When the SOS system is activated:

1. User location is captured
2. Google Maps link is generated
3. Emergency email is sent
4. SMS alert is sent to emergency contacts

<p align="center">
  <img src="https://raw.githubusercontent.com/Adithya2369/Smart-SOS-alert-system/main/block_diagram.png" width="600"/>
</p>

---

# ⚙️ Technologies Used

- Python
- Gmail SMTP
- Twilio HTTP API
- Requests Library
- USB GPS Module (NEO-6M compatible)
- Raspberry Pi

---

# 📂 Project Structure

```bash
sos.py              # Main SOS script
README.md           # Documentation
```

---

# 🖥️ Supported Modes

| Mode | Purpose | Location Source |
|------|----------|----------------|
| LAPTOP | Testing | IP-based location |
| GPS | Real deployment | USB GPS module |

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/Adithya2369/Smart-SOS-alert-system.git
cd Smart-SOS-alert-system
```

---

## Install Dependencies

### Required

```bash
pip install requests
```

### Optional (GPS Mode)

```bash
pip install pyserial
```

---

# 🔐 Configuration

Update the following fields in `sos.py`:

## Gmail Credentials

```python
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
```

---

## Emergency Contacts

```python
RECEIVER_EMAILS = [
    "guardian@gmail.com"
]
```

---

## Twilio Credentials

```python
TWILIO_SID = "your_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE = "+1XXXXXXXXXX"
```

---

# 🚀 Running the System

## Laptop Testing Mode

Set:

```python
MODE = "LAPTOP"
```

Run:

```bash
python sos.py
```

This mode:
- Uses internet-based location
- Does not require GPS hardware

---

# 🍓 Raspberry Pi Deployment

## Hardware Required

- Raspberry Pi
- USB GPS module
- Internet connection

---

## Connect GPS Module

Plug GPS into Raspberry Pi USB port.

Check device:

```bash
ls /dev/ttyUSB*
```

Example:

```bash
/dev/ttyUSB0
```

---

## Enable GPS Mode

Set:

```python
MODE = "GPS"
```

Update:

```python
GPS_PORT = "/dev/ttyUSB0"
```

Uncomment GPS-related functions in the script.

---

# 📧 Email Alert Example

```text
🚨 EMERGENCY ALERT 🚨

Time: 2026-05-10 12:30:00

Location:
17.3850, 78.4867
https://maps.google.com/?q=17.3850,78.4867
```

---

# 📱 SMS Alert Example

```text
🚨 SOS ALERT!
https://maps.google.com/?q=17.3850,78.4867
```

---

# ⚠️ Important Notes

- Twilio trial accounts can send SMS only to verified numbers
- GPS mode requires open sky access for accurate location
- Laptop mode provides approximate location only

---

# 🔒 Security Recommendations

For production deployment:

- Use environment variables
- Avoid hardcoding credentials
- Regenerate exposed API keys
- Use `.env` files

---

# 🚀 Future Enhancements

- GPIO emergency button
- Voice-trigger SOS
- Continuous location updates
- Offline caching and resend
- Cloud logging dashboard
- Mobile application integration

---

# 📜 License

This project is intended for educational and research purposes.

---

# 👨‍💻 Author

T. Adithya Reddy

---
