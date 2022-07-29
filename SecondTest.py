
# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
   
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
   
# create webdriver object
driver=webdriver.Chrome(executable_path="C:\\Users\\ramku\\Downloads\\chromedriver_win32\\chromedriver.exe");
   
# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
   
# get element 
element = driver.find_element(By.PARTIAL_LINK_TEXT,"Courses");
print("Element Attribute")
print(element.get_attribute('href'));
   
# create action chain object
action = ActionChains(driver)
   
# click the item
action.click(on_element = element)
   
# perform the operation
action.perform()