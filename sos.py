# import serial
import time
import smtplib
import requests
from requests.auth import HTTPBasicAuth
from email.mime.text import MIMEText
from datetime import datetime

# =========================
# MODE SELECTION
# =========================
MODE = "LAPTOP"   # "LAPTOP" or "GPS"

# =========================
# CONFIGURATION
# =========================

GPS_PORT = 'COM3'
BAUD_RATE = 9600

# Gmail
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

RECEIVER_EMAILS = [
    "guardian1@gmail.com",
    "guardian2@hotmail.com",
    "guardian3@proton.me"
]

# =========================
# TWILIO (HTTP API ONLY)
# =========================

TWILIO_SID = "your_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE = "+1XXXXXXXXXX"

EMERGENCY_PHONES = [
    "+911234567890",
    "+910987654321"
]

# =========================
# LAPTOP LOCATION
# =========================

def get_location_laptop():
    try:
        print("[INFO] Getting location (Laptop mode)...")
        response = requests.get("http://ip-api.com/json/")
        data = response.json()

        lat = data.get("lat")
        lon = data.get("lon")

        print(f"[SUCCESS] Location: {lat}, {lon}")
        return lat, lon

    except Exception as e:
        print(f"[ERROR] Laptop location failed: {e}")
        return None, None


# =========================
# GPS (ENABLE LATER)
# =========================

"""
def get_gps_location():
    try:
        ser = serial.Serial(GPS_PORT, BAUD_RATE, timeout=1)
        start_time = time.time()

        while True:
            line = ser.readline().decode('utf-8', errors='ignore')

            if "$GPGGA" in line or "$GPRMC" in line:
                data = line.split(',')

                if len(data) > 5 and data[2] and data[4]:
                    lat = convert_to_decimal(data[2], data[3])
                    lon = convert_to_decimal(data[4], data[5])

                    if lat and lon:
                        return lat, lon

            if time.time() - start_time > 10:
                return None, None

    except:
        return None, None


def convert_to_decimal(raw, direction):
    try:
        if direction in ['N', 'S']:
            degrees = float(raw[:2])
            minutes = float(raw[2:])
        else:
            degrees = float(raw[:3])
            minutes = float(raw[3:])

        decimal = degrees + (minutes / 60)

        if direction in ['S', 'W']:
            decimal *= -1

        return decimal  # NO rounding
    except:
        return None
"""

# =========================
# EMAIL FUNCTION
# =========================

def send_sos_email(lat, lon):
    try:
        if lat and lon:
            link = f"https://maps.google.com/?q={lat},{lon}"
            location_text = f"{lat}, {lon}\n{link}"
        else:
            location_text = "Location unavailable"

        body = f"""
🚨 EMERGENCY ALERT 🚨

Time: {datetime.now()}

Location:
{location_text}
"""

        msg = MIMEText(body)
        msg['Subject'] = "🚨 SOS Alert"
        msg['From'] = SENDER_EMAIL
        msg['To'] = ", ".join(RECEIVER_EMAILS)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, msg.as_string())
        server.quit()

        print("[SUCCESS] Email sent")

    except Exception as e:
        print(f"[ERROR] Email failed: {e}")


# =========================
# SMS VIA HTTP
# =========================

def send_sos_sms(lat, lon):
    try:
        if lat and lon:
            link = f"https://maps.google.com/?q={lat},{lon}"
            body = f"🚨 SOS ALERT! {link}"
        else:
            body = "🚨 SOS ALERT! Location unavailable"

        url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"

        for number in EMERGENCY_PHONES:
            data = {
                "From": TWILIO_PHONE,
                "To": number,
                "Body": body
            }

            response = requests.post(
                url,
                data=data,
                auth=HTTPBasicAuth(TWILIO_SID, TWILIO_AUTH_TOKEN)
            )

            if response.status_code == 201:
                print(f"[SUCCESS] SMS sent to {number}")
            else:
                print(f"[ERROR] SMS failed: {response.text}")

    except Exception as e:
        print(f"[ERROR] SMS error: {e}")


# =========================
# MAIN
# =========================

def trigger_sos():
    print("\n=== SOS ACTIVATED ===\n")

    if MODE == "LAPTOP":
        lat, lon = get_location_laptop()
    else:
        # lat, lon = get_gps_location()
        lat, lon = None, None

    send_sos_email(lat, lon)
    send_sos_sms(lat, lon)

    print("\n=== DONE ===\n")


# =========================
# RUN
# =========================

if __name__ == "__main__":
    trigger_sos()