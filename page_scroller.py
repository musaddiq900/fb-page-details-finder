from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def scroll_and_save_content(driver, site_link, output_file):
    # Open Facebook
    driver.get(site_link)

    # Wait for the page to load
    # time.sleep(5)

    # Scroll down 5 times
    for i in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait for 2 seconds between scrolls

    # Get the page source (HTML content)
    page_source = driver.page_source

    # Save the content to an HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(page_source)

    print(f"Page content saved to {output_file}")

def main(site_link):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start the browser maximized

    # Try to use Chrome driver from a specific path
    chrome_driver_path = os.path.join('./chromedriver.exe') # Update this path
    # print(chrome_driver_path)
    if os.path.exists(chrome_driver_path):
        service = Service(chrome_driver_path)
    else:
        print("ChromeDriver not found at specified path. Downloading...")
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    if __name__ =="__main__":
        # Define the output file name
        output_file = "facebook_ads_content.html"

        # Call the function to scroll and save content
        scroll_and_save_content(driver, site_link, output_file)


        # Close the browser
        driver.quit()

    else:
        # Define the output file name
        output_file = "profile.html"

        # Call the function to scroll and save content
        scroll_and_save_content(driver, site_link, output_file)


        # Close the browser
        driver.quit()





site_link ="https://google.com"

if __name__ == "__main__":
    main(site_link)