# Raspberry Pi Projects Collection

This repository contains a series of Raspberry Pi-based automation, IoT, and scripting projects that explore hardware integration, sensor data processing, and local server development. These projects demonstrate how to use Raspberry Pi as a flexible, affordable platform for real-world applications and experimentation.

## 🔧 Projects Overview

### 1. **Real-time Sensor Dashboard**
- **Tech Stack:** Python, Flask, SQLite, HTML/CSS
- **Description:** Captures temperature and humidity data from a DHT11 sensor and displays it in real-time on a web dashboard.
- **Features:**
  - Automatic sensor polling and local data storage
  - Real-time chart rendering with auto-refresh
  - Easy deployment on Pi as a local server

### 2. **Home Automation Script**
- **Tech Stack:** Python, Shell
- **Description:** Automates control of lights or appliances via GPIO pins using scheduled scripts or trigger-based actions.

### 3. **Camera Motion Detection**
- **Tech Stack:** Python, OpenCV
- **Description:** Uses a connected camera module to detect motion and log images or videos for home surveillance.

## 🚀 Getting Started

### Prerequisites
- Raspberry Pi 3/4 with Raspbian OS
- Python 3.x
- GPIO libraries (`RPi.GPIO`, `Adafruit_DHT`, etc.)
- Flask for web dashboard (optional)

### Setup
```bash
git clone https://github.com/Prakash-sa/Raspberry-Pi.git
cd Raspberry-Pi
pip install -r requirements.txt
```
