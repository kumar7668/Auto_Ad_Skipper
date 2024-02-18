from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to ChromeDriver executable
chrome_driver_path = r'./ch_driver/chromedriver'

# Path to the user data directory
user_data_dir = 'C:/Users/user/AppData/Local/Google/Chrome/User Data'

# URL of the YouTube video
video_url = "https://www.youtube.com/"

# Initialize ChromeDriver with user data directory
chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + user_data_dir)

# Open the YouTube video
driver = webdriver.Chrome( options=chrome_options)

# Define a function to skip ads
def skip_ads():
    try:
        skip_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Skip Ad']"))
        )
        skip_button.click()
        print("Skip button clicked.")
    except:
        print("Skip button not found or not clickable.")

# Main loop to continuously skip ads
while True:
    try:
        skip_ads()
    except KeyboardInterrupt:
        print("Script stopped by user.")
        break

# Close the browser
driver.quit()
