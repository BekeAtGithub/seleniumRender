import time  # Used for time delays
import json  # JSON data handling
import os  # For environment variables

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings

# --------------------- SETUP SELENIUM ---------------------
edge_options = Options()
edge_options.add_argument("--headless")  # Enable headless mode (no GUI)
edge_options.add_argument("--disable-gpu")  # Disable GPU acceleration
edge_options.add_argument("--window-size=1920x1080")  # Specify window size

# Microsoft Edge WebDriver path
edge_driver_path = r"<replace with edge webdriver path>"

service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# --------------------- LOAD THE WEBSITE ---------------------
url = "<replace with url>"
driver.get(url)
time.sleep(10)  # Wait for the page to fully load

# --------------------- CHECK IF ELEMENTS EXIST ---------------------
print("Checking if departments are available on the page...")

# Print the page source for debugging (Uncomment if needed)
# print(driver.page_source)

# Look for all department elements using XPath
departments = driver.find_elements(By.XPATH, "//div[contains(@class, '<class name>')]")
print(f"Found {len(departments)} department elements.")

# If no departments were found, print the page source for debugging
if len(departments) == 0:
    print("No departments found! Possible causes:")
    print("- The website loads data dynamically (try increasing `time.sleep(10)`)")
    print("- The XPath or class names are incorrect")
    print("- The data is inside an `iframe` (checking next...)")

    # Check if an iframe exists
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Found {len(iframes)} iframes on the page.")

    if len(iframes) > 0:
        print("Attempting to switch to the first iframe...")
        driver.switch_to.frame(iframes[0])  # Switch to the first iframe
        time.sleep(3)  # Wait for iframe content to load

        # Try extracting departments again inside the iframe
        departments = driver.find_elements(By.XPATH, "//div[contains(@class, '<classname>')]")
        print(f"After switching iframe: Found {len(departments)} department elements.")
    
    if len(departments) == 0:
        print("Still no departments found. Exiting...")
        driver.quit()
        exit()

# --------------------- EXTRACT DATA ---------------------
data = []

for dept in departments:
    # Extract department name (<replace with dept_name>)
    try:
        dept_name = dept.text.strip()
        print(f"Found department: {dept_name}")
    except:
        dept_name = "N/A"

    #Extract department percentage using XPath
    try:
        dept_percent = dept.find_element(By.XPATH, ".//following-sibling::div[contains(@class, '<class name for percent>') and contains(@class, '<class name for percent>')]").text
        print(f"Percentage: {dept_percent}")
    except:
        dept_percent = "N/A"

    # Store department data
    data.append({
        "type": "department",
        "name": dept_name,
        "percentage": dept_percent
    })

# Switch back to the main page if we switched to an iframe
driver.switch_to.default_content()

# Quit the Selenium WebDriver after rendering page
driver.quit()

# --------------------- SET UP LLAMAINDEX WITH OPENAI ---------------------
# OpenAI API configuration
api_endpoint = "<replace with api endpoint>"
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI LLM
llm = OpenAI(api_key=api_key, base_url=api_endpoint)

# Use LlamaIndex settings for API
Settings.llm = llm  

# --------------------- STRUCTURE DATA INTO JSON ---------------------
structured_data = {
    "summary": "Extracted performance analytics data",
    "entries": data
}

# Save to a JSON file
output_file = "analytics_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(structured_data, f, indent=4)

print(f"Data successfully saved to {output_file}")
