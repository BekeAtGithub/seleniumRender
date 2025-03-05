import time  # used for time delays
import json  # json data handling
from selenium import webdriver  # utilize Selenium WebDriver with edge
from selenium.webdriver.common.by import By  # finding javascript front end elements, which are in the inspect tab
from selenium.webdriver.edge.service import Service  # Microsoft Edge service
from selenium.webdriver.edge.options import Options  # Microsoft Edge options
from llama_index.llms.openai import OpenAI  # OpenAI for LlamaIndex processing
from llama_index.core.settings import Settings  # Use updated settings API

# --------------------- SETUP SELENIUM ---------------------
edge_options = Options()
edge_options.add_argument("--headless")  # enable headless mode aka no Graphical user interface
edge_options.add_argument("--disable-gpu")  # disable GPU acceleration
edge_options.add_argument("--window-size=1920x1080")  # specify window size

# Microsoft Edge WebDriver path 
edge_driver_path = r"< replace with your local driver location>"

service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# --------------------- LOAD THE WEBSITE ---------------------
url = "<replace with url>"  # URL to render
driver.get(url)
time.sleep(5)  # utilize delay to wait for page to fully load

# --------------------- EXTRACT DATA ---------------------
data = []  # pre-created list to store extracted data

# Extract all department names and their percentages
departments = driver.find_elements(By.CLASS_NAME, "replace with element class name")  # Element class name for department
for dept in departments:
    dept_name = dept.find_element(By.CLASS_NAME, "replace with object of the class").text  # individual object of department class
    dept_percent = dept.find_element(By.CLASS_NAME, "replace with object displaying percentage").text  # Get percentage of the individual objects

    # Store department data
    data.append({
        "type": "department",
        "name": dept_name,
        "percentage": dept_percent
    })

    # Click on the department to open employee details
    dept.click()
    time.sleep(3)  # Allow page to update

    # Extract employee names and their percentages within the department
    employees = driver.find_elements(By.CLASS_NAME, "emp-class")  # Element class name for employee
    for emp in employees:
        emp_name = emp.find_element(By.CLASS_NAME, "emp-name").text  # individual employee name 
        emp_percent = emp.find_element(By.CLASS_NAME, "emp-percentage").text  # Get percentage of individual employees

        # Store employee data
        data.append({
            "type": "employee",
            "name": emp_name,
            "department": dept_name,
            "percentage": emp_percent
        })

# quit the Selenium WebDriver after rendering page
driver.quit()

# --------------------- SET UP LLAMAINDEX WITH OPENAI ---------------------
# OpenAI API configuration
import os
api_endpoint = "replace with api endpoint"
api_key = os.getenv("OPENAI_API_KEY")  # "OPEN_API_KEY" is an environment variable, go to VS CLI and type in: set OPEN_API_KEY='string'


# Initialize OpenAI LLM
llm = OpenAI(api_key=api_key, base_url=api_endpoint) 


# Use llama llm Settings for API
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
