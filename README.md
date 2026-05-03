# ATM Security System Web Interface

This project provides a web interface for an ATM security system that uses facial recognition to detect unauthorized access attempts. The system allows administrators to approve or ban detected users and monitor system status.

## Features

- **Admin Login**: Secure access to the management interface
- **User Management**: Approve or ban users detected by the system
- **Real-time Alerts**: Immediate notifications of unauthorized access attempts
- **Dark Mode UI**: Toggle between light and dark themes
- **Live WebSocket Notifications**: Real-time updates without page refresh
- **Minimalist & Professional Design**: Clean, responsive interface

## Components

The system consists of three main components:

1. **Detection Script** (`detection.py`): Python script that uses facial recognition to detect and identify people
2. **Alert System** (`alerts.py`): Manages notifications and user authorization status
3. **Web Interface** (`app.py`): Flask web application for managing the security system

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- OpenCV
- InsightFace
- Flask
- Flask-SocketIO
- Twilio (for SMS notifications)
- SMTP access (for email notifications)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/atm-security-system.git
   cd atm-security-system
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file with the following variables:
   ```
   EMAIL_SENDER=your-email@gmail.com
   EMAIL_PASSWORD=your-email-password
   TWILIO_ACCOUNT_SID=your-twilio-sid
   TWILIO_AUTH_TOKEN=your-twilio-token
   TWILIO_PHONE_NUMBER=your-twilio-phone
   SECRET_KEY=your-flask-secret-key
   API_URL=http://localhost:5000/api
   ```

4. Initialize the database:
   ```
   python app.py
   ```

### Running the System

1. Start the Flask web application:
   ```
   python app.py
   ```

2. In a separate terminal, run the detection script:
   ```
   python detection.py
   ```

3. Access the web interface at `http://localhost:5000`

## Usage

1. **Login**: Use the default credentials (admin/admin123) to access the system
2. **Dashboard**: View system status and recent alerts
3. **Alerts**: Manage unauthorized access attempts
4. **Users**: View and manage authorized and banned users
5. **Settings**: Configure system settings

## Integration with Detection System

The `integration.py` module provides functions to connect the detection script with the web application:

- `register_alert(face_id)`: Register a new unauthorized access alert
- `get_status(face_id)`: Check if a user has been approved or banned

To modify your existing `detection.py` script to work with the web interface:

1. Import the integration module:
   ```python
   import integration
   ```

2. Replace the `alerts.get_status()` call with:
   ```python
   integration.get_status(face_id)
   ```

3. Add an alert registration after detection:
   ```python
   integration.register_alert(face_id)
   ```

## Default Credentials

- Username: `admin`
- Password: `admin123`
