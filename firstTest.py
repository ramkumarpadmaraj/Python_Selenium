
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\ramku\\Downloads\\chromedriver_win32\\chromedriver.exe");
driver.get("https://www.rcvacademy.com/");

elements=driver.find_elements(By.TAG_NAME,'a');
for element in elements:
    print("Element Attribute");
    print(element.get_attribute('href'));
count=elements.count;
print("Count is displayed below");
print(count);
