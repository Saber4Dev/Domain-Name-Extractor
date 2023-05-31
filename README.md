Project Domain Extractor and Website Screenshot Capture
This Python script allows you to extract domain names from project text files and capture screenshots of the corresponding websites. It is designed to work with a specific folder structure where each project has a corresponding text file containing project information, including the desired domain name. The script extracts the domain names and saves them to a text file. It also captures website screenshots in full resolution and saves them in a "Site web preview" folder.

Features
Extracts domain names from project text files based on a specific line pattern.
Captures screenshots of the corresponding websites in full resolution (1920x1080).
Skips inaccessible websites or websites with invalid domain names.
Organizes screenshots in a dedicated folder named "Site web preview".
Saves the extracted domain names and company names to a text file.
Requirements
Python 3.x
Selenium (install using pip install selenium)
ChromeDriver (download from: https://sites.google.com/a/chromium.org/chromedriver/)
Usage
Set up the folder structure as follows:

Copy code
Projects/
├── Project 1/
│   ├── Project 1.txt
├── Project 2/
│   ├── Project 2.txt
├── ...
Update the script's variables:

Set the path variable to the path of the "Projects" folder.
Set the chromedriver_path variable to the path of the ChromeDriver executable.
Run the script using the command: python extract_dns_screenshot.py

The extracted domain names will be saved in a file named "Domain name.txt" in the "Projects" folder.

The captured website screenshots will be saved in the "Site web preview" folder.

License
This script is licensed under the MIT License.

Feel free to modify and adapt it to your needs.
