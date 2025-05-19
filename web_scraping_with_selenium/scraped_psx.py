# import csv
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# options=Options()

# path = r'C:\chromedriver\chromedriver.exe'
# driver = webdriver.Chrome(path)
# driver.get('https://www.psx.com.pk/market-summary/')
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# time.sleep(5)
# table = driver.find_elements(By.TAG_NAME,'table')
# with open('psx.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['CompanyName', 'Ldcp', 'Open', 'High', 'Low', 'Current', 'Change', 'Volume'])

#     for tab in table[2:]:
#         rows = tab.find_elements(By.TAG_NAME, 'tr')
#         for row in rows:
#             data = row.find_elements(By.TAG_NAME, 'td')
#             if len(data) >= 8:
#                 company_name = data[0].text
#                 ldcp = data[1].text
#                 open_price = data[2].text
#                 high = data[3].text
#                 low = data[4].text
#                 current = data[5].text
#                 change = data[6].text
#                 volume = data[7].text
#                 writer.writerow([company_name, ldcp, open_price, high, low, current, change, volume])
#                 print(company_name,ldcp,open_price,high,low,current,change,volume)

# driver.quit()



import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Specify the path to your chromedriver
path = r'C:\chromedriver\chromedriver.exe'

# Create a Service object
service = Service(path)

# Set up Chrome options (if needed)
options = Options()

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Open the target website
driver.get('https://www.psx.com.pk/market-summary/')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)

# Locate the table elements
table = driver.find_elements(By.TAG_NAME, 'table')

# Save data to a CSV file
with open('psx.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['CompanyName', 'Ldcp', 'Open', 'High', 'Low', 'Current', 'Change', 'Volume'])

    for tab in table[2:]:
        rows = tab.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            data = row.find_elements(By.TAG_NAME, 'td')
            if len(data) >= 8:
                company_name = data[0].text
                ldcp = data[1].text
                open_price = data[2].text
                high = data[3].text
                low = data[4].text
                current = data[5].text
                change = data[6].text
                volume = data[7].text
                writer.writerow([company_name, ldcp, open_price, high, low, current, change, volume])
                print(company_name, ldcp, open_price, high, low, current, change, volume)

# Quit the driver
driver.quit()
