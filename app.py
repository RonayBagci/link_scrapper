
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

keyword = "Python" # You can use another keyword
driver.get(f"https://www.google.com/search?q={keyword}")

time.sleep(2)

search_results = driver.find_elements(By.XPATH, "//a[@href and @data-ved]")

links = []

for result in search_results:
    link = result.get_attribute('href')
    if link not in links:
        links.append(link)

with open("links.txt", "w") as file:
    for link in links:
        file.write(link + "\n")

driver.quit()

print("Number of links: ",len(links))
