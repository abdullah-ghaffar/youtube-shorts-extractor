import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def extract_shorts_links(channel_url):
    """Extracts YouTube Shorts video links from a given channel URL."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run headless for faster performance
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get(channel_url)
    time.sleep(5)  # Allow time for the page to load

    shorts_links = []
    
    # Scrolling to load all shorts
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    
    while True:
        # Extract links
        videos = driver.find_elements(By.XPATH, '//a[@href and contains(@href, "/shorts/")]')
        
        for video in videos:
            link = video.get_attribute('href')
            if link not in shorts_links:  # Avoid duplicates
                shorts_links.append(link)
        
        # Scroll down
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)  # Wait for new content to load

        # Check for new content
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    driver.quit()
    return shorts_links

def save_links_to_file(links, file_path):
    """Save the list of links to a text file."""
    try:
        with open(file_path, 'w') as file:
            for link in links:
                file.write(f"{link}\n")
        print(f"Links successfully saved to {file_path}.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
