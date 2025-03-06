
![alt text](https://github.com/BekeAtGithub/seleniumRender/blob/main/seleniumRender.jpg)

## **📌 Purpose**
This script extracts **department performance data** and **employee performance data** from a **JavaScript-rendered website**. It then **processes the data using LlamaIndex with OpenAI** and saves the structured output in **JSON format**.

---

## **🔧 Technologies Used**
| Technology    | Purpose |
|--------------|---------|
| **Python** | Scripting and automation |
| **Selenium** | Browser automation to interact with JavaScript-rendered pages |
| **Microsoft Edge WebDriver** | Controls the Edge browser via Selenium |
| **LlamaIndex (Llama Agent)** | Uses OpenAI LLM to process extracted data |
| **OpenAI API** | Provides AI-powered analysis capabilities |
| **JSON** | Stores extracted and processed data in structured format |
| **CSS Selector** | Is run by the selenium-css-selector.py file |
| **XPATH** | Is run by the selenium-xpath.py file

- **CSS Selector:** A **pattern-based selector** used to find elements in HTML by matching class names, IDs, attributes, or element types, making it **faster and more readable** but **less flexible** for complex structures.  
- **XPath:** A **tree-based path query language** used to navigate through the entire DOM structure, allowing for **advanced selection** based on relationships (parent, child, sibling), but it **can be slower** than CSS selectors.|

---

## **📂 File Structure**
```
project-folder/
│── edgedriver_win64/        # Edge WebDriver (msedgedriver.exe)
│── selenium-css-selector.py # CSS selector script
│── selenium-xpath.py        # xpath script
│── analytics_data.json      # Extracted output data
│── README.md                # Documentation
│── venv/                    # Python virtual environment
```

---

## **🚀 How It Works**
1. **Load the website**  
   - The script uses **Selenium** to open the given **URL** in a **headless Edge browser**.  
   - It waits for the page to fully load.  

2. **Extract department data**  
   - Finds department elements based on their **HTML class names**.  
   - Extracts department **names** and **performance percentages**.  

3. **Extract employee data**  
   - Clicks on each department to expand its details.  
   - Extracts each **employee’s name** and **individual performance percentage**.  

4. **Process data using LlamaIndex**  
   - Configures **OpenAI API** for LlamaIndex.  
   - Stores extracted data in a **structured JSON format**.  

5. **Save data in JSON file**  
   - Data is written to `analytics_data.json`.  
   - The file can be used for further **analysis or reporting**.  

---

## **🖥️ Prerequisites**
Before running the script, ensure you have the following installed:  
✅ **Python (>=3.8)** – [Download Here](https://www.python.org/downloads/)  
✅ **Edge WebDriver** – [Download Here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
✅ **Required Python Packages** (install using `pip`):
```sh
pip install selenium llama-index openai
```
✅ **Set up OpenAI API Key**:
```sh
set OPENAI_API_KEY=your-api-key  # Windows
export OPENAI_API_KEY=your-api-key  # Mac/Linux
```

---

## **🛠 How to Run**
1. **Ensure Edge WebDriver is installed**  
2. **Update the class names** in `selenium_forest.py` to match your website’s structure.  
3. **Run the script**:
   ```sh
   python selenium-css-selector.py // OR selenium-xpath.py
   ```
4. **Check the output in `analytics_data.json`**.

---

## **🔧 Sources Used**
https://learn.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp 

https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH

https://www.selenium.dev/documentation/webdriver/

https://selenium-python.readthedocs.io/

https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/?utm_source=chatgpt.com#parsing-the-html-with-beautiful-soup

https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/?utm_source=chatgpt.com

https://www.w3schools.com/xml/xpath_intro.asp#:~:text=Learn%20how%20to%20use%20%EE%80%80XPath%EE%80%81%20to%20navigate%20and

https://docs.llamaindex.ai/en/stable/getting_started/starter_example/
