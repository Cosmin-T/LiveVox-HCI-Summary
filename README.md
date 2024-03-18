# LiveVox HCI Agent Summary Report Automation

**IMPORTANT:** This serves as an informative repository with no need for installation, as there is no** **.env file, and the automation is designed for a specific website inaccessible to anyone.

This project automates the generation and processing of HCI (Human-Computer Interaction) agent summary reports from LiveVox, a cloud-based contact center platform. It utilizes Selenium for web scraping, pandas for data processing, and smtplib for email notifications.

## Prerequisites

- Python 3.x
- Chrome Web Browser
- Chromedriver
- Python packages specified in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/livevox-hci-automation.git
   cd livevox-hci-automation
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables:

   Create a `.env` file in the root directory and define the following variables:

   ```dotenv
   USER=your_livevox_username
   PASSWORD=your_livevox_password
   OUTLOOK_TEMPLATE=your_outlook_template
   URL=livevox_url
   RECEIVER_EMAIL=recipient_email_address
   SENDER_EMAIL=your_email_address
   GMAIL_APP_PASSWORD=your_app_password_for_gmail
   ```

## Usage

1. Execute the main script:

   ```bash
   python3 main.py
   ```
2. The script will:

   - Initialize the Chrome webdriver and log in to LiveVox.
   - Navigate to the agent summary report section.
   - Add dates for report generation.
   - Generate reports for each HCI agent.
   - Process and append data to Excel files.
   - Send email notifications with attached reports.
   - Clean up downloaded files.

## File Structure

- `logic/`: Contains Python modules for different functionalities.
  - `util.py`: Contains utility functions and configuration variables.
  - `login.py`: Handles logging in to LiveVox.
  - `navigation.py`: Implements navigation through LiveVox interface.
  - `dates.py`: Manages date selection for report generation.
  - `process.py`: Processes and appends data to Excel files.
  - `send_email.py`: Sends email notifications with reports.
  - `webdriver.py`: Initializes the Chrome webdriver.
  - `main.py`: Main script orchestrating the automation process.
- `requirements.txt`: Lists required Python packages.
- `.env.example`: Example environment variable configuration file.

## Notes

- Make sure to customize environment variables and file paths according to your setup.
- Chromedriver path (`CROMEDRIVER_PATH`) and other file paths may need adjustments based on your system configuration.
- Ensure that your LiveVox account credentials and email settings are correctly configured in the `.env` file.
