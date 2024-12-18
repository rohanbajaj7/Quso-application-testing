from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

def wait_for_page_load(driver, until=lambda driver: driver.execute_script("return document.readyState") == "complete", timeout=20):
    return WebDriverWait(driver, timeout).until(until)

# Modified click function to check if the element is enabled before clicking
def click(driver, by, value, retries=3):
    element = None
    while retries > 0:
        try:
            element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
            
            if element.is_enabled():
                element.click()
                return element
            else:
                print("Button is disabled, retrying...")
        except Exception as e:
            print(f"Click intercepted or timeout: {e}. Retrying...")
            retries -= 1
            time.sleep(2)
    return None

driver = webdriver.Chrome()

try:
    driver.get("https://app.quso.ai/auth/login-with-email")
    logging.info("Opened Quso.ai application.")
    wait_for_page_load(driver)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="e.g johndoe@gmail.com"]'))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Enter your password"]'))
    )

    username_field.send_keys("vikram0812+niit@proton.me")
    password_field.send_keys("NIIT@2024")
    password_field.send_keys(Keys.RETURN)

    logging.info("Logged in successfully.")

    # Navigate to AI Video Generator
    ai_generator = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'create-ai-video-generator'))
    )
    ai_generator.click()

    generate_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Briefly summarize your script in a few words or sentences..."]'))
    )
    
    generate_field.send_keys("What if I told you that the best friendships are built on the craziest adventures? Meet Sarah and Jake...")
    
    generate_field_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'describe-script-continue-button'))
    )
    
    generate_field_button.click()

    generate_field_button_final = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'text-to-video-generate-video-button'))
    )

    click(driver, By.ID, 'text-to-video-generate-video-button')

    generate_field_button_final1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'text-to-video-generate-video-button'))
    )
    click(driver, By.ID, 'text-to-video-generate-video-button')
    driver.get("https://app.quso.ai/all-projects") 
    driver.get("https://app.quso.ai/ai-text-to-video/preview?project_id=861f6603-7d4d-4d41-86b6-b364851e3248")
    click(driver, By.ID, 'text-to-video-download-button')
    time.sleep(40)
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    # Close the browser
    driver.quit()
    logging.info("Automation script completed.")
