
![alt text]([https://github.com/BekeAtGithub/seleniumRender/blob/main/seleniumRender.jpg])

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

---

## **📂 File Structure**
```
project-folder/
│── edgedriver_win64/        # Edge WebDriver (msedgedriver.exe)
│── selenium_forest.py       # Main Python script
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
   python selenium_forest.py
   ```
4. **Check the output in `analytics_data.json`**.

---
