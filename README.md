Selenium Automation Script for Quso.ai Video Generation
This Python script automates the process of logging into Quso.ai, generating a video through the AI Video Generator, and downloading the generated video. The script utilizes Selenium WebDriver to interact with the web page and perform tasks such as logging in, entering a script, clicking buttons, and downloading the video.

Features
Automated Login: Logs into Quso.ai with a username and password.
AI Video Generation: Navigates through the AI Video Generator and submits a predefined video script.
Video Download: Downloads the generated video to the local system.
Error Handling and Logging: Implements basic error handling and logs the progress of each step.
Prerequisites
Before running the script, ensure you have the following:

Python 3.x: This script is written in Python 3. Install it from python.org.
Selenium: Selenium WebDriver for automating browser actions.
ChromeDriver: WebDriver for the Chrome browser. Ensure its version is compatible with your installed Chrome version.
Chrome Browser: This script uses Chrome, so it should be installed and up to date.
Installing Dependencies
Install Python 3.x: Download and install Python 3 from python.org.

Install Selenium: To install Selenium, run the following command in your terminal or command prompt:

bash
Copy code
pip install selenium
Download ChromeDriver:

Download the appropriate version of ChromeDriver from here.
Make sure the version of ChromeDriver matches your installed version of Chrome.
Add chromedriver to your system's PATH or specify its location directly in the script.
Script Overview
This script performs the following automated tasks:

Logs into Quso.ai: The script logs into the Quso.ai application using the specified username and password. Replace the values with your own credentials:

python
Copy code
username_field.send_keys("your_email@example.com")
password_field.send_keys("your_password")
Navigates to AI Video Generator: After logging in, the script navigates to the AI Video Generator page.

Enters Video Script: The script enters a predefined script into a text field to create a new video:

python
Copy code
generate_field.send_keys("What if I told you that the best friendships are built on the craziest adventures? Meet Sarah and Jake...")
Generates the Video: The script generates the video by clicking the "Generate Video" button multiple times.

Downloads the Video: After navigating to the project preview page, the script clicks the download button to save the generated video:

python
Copy code
click(driver, By.ID, 'text-to-video-download-button')
Error Handling and Logging: The script includes basic error handling, logging any issues that may arise during execution.

How to Use
1. Clone the Repository
If you haven't already cloned the repository, you can do so with the following command:

bash
Copy code
git clone <repository-url>
cd <project-directory>
2. Modify Credentials (if necessary)
Before running the script, make sure to replace the username and password fields with your own credentials:

python
Copy code
username_field.send_keys("your_email@example.com")
password_field.send_keys("your_password")
3. Run the Script
After cloning the repository and making the necessary modifications, run the script using the following command:

bash
Copy code
python automation_script.py
The script will open a Chrome browser, log in to Quso.ai, generate a video, and download it.

4. Expected Behavior
The script opens a Chrome browser window and navigates through the process of logging in, generating a video, and downloading it.
Logs are generated to track each step of the process, and any errors are displayed in the terminal.
Troubleshooting
ChromeDriver Version Mismatch: If you encounter an error related to ChromeDriver, make sure the version of ChromeDriver matches the version of your Chrome browser. You can download the appropriate version of ChromeDriver here.

Login Issues: Ensure your email and password are correctly entered in the script. Double-check if the login page selectors or placeholders have changed.

Webpage Structure Change: If the page structure or element IDs change on Quso.ai, you may need to update the script’s element locators (By.ID, By.CSS_SELECTOR, etc.) to reflect the new structure.

License
This project is licensed under the MIT License - see the LICENSE file for details.
