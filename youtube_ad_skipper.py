import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep

class YoutubePlayer:

    # URL of YouTube
    url = "https://www.youtube.com/"

    def __init__(self):
        '''
        # Initialize Chrome webdriver {odd way-1}
        # self.driver = webdriver.Chrome(executable_path=r'./ch_driver/chromedriver.exe')

        # Initialize Chrome webdriver {odd way -2}
        # If Chrome webdriver path is already having in you system path
        # self.driver = webdriver.Chrome()
        
        '''

        # Initialize Chrome webdriver and set up logging
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.total_skip_ad = 0
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def check_ad(self):
        try:
            # Wait for the ad-player/skip button container to appear
            ad_overlay = WebDriverWait(self.driver, 8).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".ytp-ad-player-overlay"))
            )
            # Return the ad overlay element if found
            return ad_overlay
        except TimeoutException:
            # If ad overlay doesn't appear within 8 seconds, return None
            return None

    def skip_ad(self):
        try:
            # Check if ad overlay is present
            ad_overlay = self.check_ad()
            if ad_overlay:
                logging.info("Ad overlay detected, scrolling to bring it into view...")
                # Find and click the skip button
                btn_for_skip = self.driver.find_element(By.CSS_SELECTOR, ".ytp-ad-skip-button-container")
                btn_for_skip.click()
                logging.info("Ad skipped successfully")
                self.total_skip_ad += 1
                logging.info("Skipped %d ads so far", self.total_skip_ad)
                sleep(1)  # Add a short delay
        except NoSuchElementException:
            logging.info("No ad overlay found, continuing...")
        except Exception as e:
            logging.error("An error occurred while skipping ad: %s", str(e))


if __name__ == "__main__":
    # Create an instance of YoutubePlayer
    youtube = YoutubePlayer()
    # Open YouTube in the web browser
    youtube.driver.get(youtube.url)

    # Continuously check for ads and skip them if found
    while True:
        # Check if ad overlay is present
        ad_overlay = youtube.check_ad()
        if ad_overlay:
            # If ad overlay is found, skip the ad
            youtube.skip_ad()
        else:
            # If no ad overlay is found, continue checking
            logging.info("No ad detected, continuing...")
        sleep(2)  # Check for ads every 2 seconds
