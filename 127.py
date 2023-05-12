from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# URL
start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

# Web Driver
browser = webdriver.Chrome("D:/Python/C127/chromedriver.exe")
browser.get(start_url)

# Delay
time.sleep(10)

planets_data = []

def scrap():
    for i in range(0, 10):
        print(f'scrapping page {i+1}')
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planets_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a')
scrap()

headers = ["name", "light_years_from_earth", "planet_mars", "stellar_magnitude", "discovery_date"]
planet_df = pd.DataFrame(planets_data, columns = headers)
planet_df.to_csv("C127/Scrapped_Data.csv", index=True, index_label="id")
    
