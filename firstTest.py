
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome(executable_path="C:\\Users\\ramku\\Downloads\\chromedriver_win32\\chromedriver.exe", options=options);
driver.get("https://www.a2hosting.com/kb/getting-started-guide/internet-and-networking/checking-your-website-for-broken-links");
time.sleep(3);
elements=driver.find_elements(By.TAG_NAME,'a');

print("Count is displayed below :" + str(len(elements)));
#print(count);
valid_url_count=0;
invalid_url_count=0;
invalid_url=[];
for element in elements:
   # print("Element Attribute");
   # print(element.get_attribute('href'));
    status_code=0;
    try: 
        req=requests.get(element.get_attribute('href'));
        status_code=req.status_code;
        valid_url_count+=1;
    except Exception as ex:
        print(ex);
        invalid_url_count+=1;
           
print("Valid URL Count " + str(valid_url_count));
print("Invalid URL Count " + str(invalid_url_count));
print(invalid_url);

driver.close();

