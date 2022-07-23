
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\ramku\\Downloads\\chromedriver_win32\\chromedriver.exe");
driver.get("https://google.com/");
element=driver.find_element(By.NAME,"q");
print(element.get_attribute("title"));
element.send_keys("python");
element.send_keys(Keys.RETURN);

