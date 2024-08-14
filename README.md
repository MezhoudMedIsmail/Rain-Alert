
# Weather Alert Script

This Python script checks the weather forecast for a specific location using the OpenWeatherMap API and sends an SMS alert via Twilio if rain is expected. 

## Features

- Fetches weather data for a specified location.
- Sends an SMS alert if rain is forecasted.
- Securely handles API credentials using environment variables.

## Prerequisites

- Python 3.x
- An account with [OpenWeatherMap](https://openweathermap.org/api) for the API key.
- An account with [Twilio](https://www.twilio.com/) for sending SMS messages.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-alert-script.git
   cd weather-alert-script
   ```

2. Install the required packages:
   ```bash
   pip install requests twilio
   ```

3. Set up your environment variables:
   - `OWM_API_KEY`: Your OpenWeatherMap API key.
   - `AUTH_TOKEN`: Your Twilio Auth Token.
   - `https_proxy`: (If needed) Your proxy setting.

## Usage

1. Update the `lat` and `lon` variables in the script with your desired location's coordinates.

2. Replace the placeholders for `from_` and `to` with your Twilio number and your verified phone number.

3. Run the script:
   ```bash
   python weather_alert.py
   ```

If rain is forecasted, you'll receive an SMS alert.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/)
- [Twilio](https://www.twilio.com/)

---

This README provides an overview, setup instructions, and usage guidelines for your script. Feel free to customize it further based on your needs!
