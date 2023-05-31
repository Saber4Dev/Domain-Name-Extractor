import os
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

# Path to the directory containing all project folders
path = "C:/Users/user/Desktop/Projects"

# Regular expressions to match the desired lines
line_regex = r"Nom de l'entreprise sur le site web\s*:\s*(.+)"
domain_regex = r"Nom de domaine souhaité\s*:\s*(.+)"

# List to store the extracted domain names and company names
results = []

# Configure Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
chrome_options.add_argument("--start-maximized")  # Maximize the browser window
chrome_options.add_argument("--window-size=1920,1080")  # Set the window size to 1920x1080 pixels
chrome_options.add_argument("--disable-infobars")  # Disable the "Chrome is being controlled by automated test software" infobar
chrome_options.add_argument("--disable-dev-shm-usage")  # Disable the /dev/shm usage to prevent Chrome crashes
chrome_options.add_argument("--no-sandbox")  # Disable the sandbox mode

# Path to the ChromeDriver executable (Download from: https://sites.google.com/a/chromium.org/chromedriver/)
chromedriver_path = "C:/path/to/chromedriver"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Create the "Site web preview" folder if it doesn't exist
screenshot_folder = os.path.join(path, "Site web preview")
os.makedirs(screenshot_folder, exist_ok=True)

# Loop through all project folders
for project_folder in os.listdir(path):
    # Get path to the project folder
    project_folder_path = os.path.join(path, project_folder)

    # Check if it's a directory
    if not os.path.isdir(project_folder_path):
        continue

    # Get the project name (without the "txt" extension)
    project_name = project_folder + ".txt"

    # Search for the text file within the project folder
    text_file_path = os.path.join(project_folder_path, project_name)

    # Continue to the next project folder if no text file is found
    if not os.path.exists(text_file_path):
        print(f"No text file found for project: {project_folder}")
        continue

    # Read contents of the text file using different encodings
    text = None
    for encoding in ["utf-8", "latin-1"]:
        try:
            with open(text_file_path, "r", encoding=encoding) as f:
                text = f.read()
            break
        except UnicodeDecodeError:
            continue

    if text is None:
        print(f"Failed to read the text file: {text_file_path}")
        continue

    # Find the desired lines using the regex
    domain_match = re.search(domain_regex, text)
    company_match = re.search(line_regex, text)

    if domain_match and company_match:
        domain_name = domain_match.group(1)
        company_name = company_match.group(1)

        if domain_name.strip() != "":
            result = f"{company_name} - {domain_name}"
            results.append(result)

            # Open the website and capture a screenshot
            url = f"https://{domain_name}"

            try:
                driver.get(url)
                time.sleep(5)  # Wait for the page to load (adjust this if needed)

                # Check if the website is accessible
                if "This site can't be reached" in driver.title:
                    print(f"Skipping inaccessible website: {domain_name}")
                    continue

                # Capture a screenshot and save it in the "Site web preview" folder
                screenshot_name = f"{company_name}-capture.png"
                screenshot_path = os.path.join(screenshot_folder, screenshot_name)
                driver.save_screenshot(screenshot_path)
            except WebDriverException as e:
                print(f"Error capturing screenshot for {domain_name}: {str(e)}")
                continue

# Close the Chrome driver
driver.quit()

# Export domain names and company names to a text file
output_file = os.path.join(path, "Domain name.txt")
with open(output_file, "w", encoding="utf-8") as f:
    for result in results:
        f.write(result + "\n")

print("Domain names extracted successfully and saved to 'Domain name.txt'.")
print("Website screenshots captured successfully.")
