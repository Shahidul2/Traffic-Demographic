from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

def get_traffic_data(driver):

    data, total_rows_needed = set(), 500

    while len(data) < total_rows_needed:
        rows = driver.find_elements(By.CSS_SELECTOR, "div.ReactVirtualized__Grid__innerScrollContainer > a")

        for row in rows:
            try:
                rank = row.find_element(By.CSS_SELECTOR, "span.sc-a983f410-4").text.strip()
                city, country = row.find_element(By.CSS_SELECTOR, "div.sc-d29a5f30-0").text.strip().split("\n")
                avg_time = row.find_element(By.CSS_SELECTOR, "span.sc-a983f410-5").text.strip()
                change = row.find_element(By.CSS_SELECTOR, "div.sc-12ceba03-0").text.strip()
                congestion = row.find_elements(By.CSS_SELECTOR, "div.sc-a983f410-8")[0].text.strip()
                lost_time = row.find_elements(By.CSS_SELECTOR, "div.sc-a983f410-8")[1].text.strip()
                rank_congestion = row.find_elements(By.CSS_SELECTOR, "span.sc-a983f410-7")[-1].text.strip()

                data.add((rank, city, country, avg_time, change, congestion, lost_time, rank_congestion))
            except:
                continue

        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)

    return list(data)

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.tomtom.com/traffic-index/ranking/")
    time.sleep(5)

    df = pd.DataFrame(get_traffic_data(driver), 
                      columns=["Rank", "City", "Country", "Average Travel Time", "Change from 2023", 
                               "Congestion Percentage", "Time Lost Per Year", "Congestion Rank"])

    df.to_csv("traffic_index_data.csv", index=False)
    print("Data saved to traffic_index_data.csv!")
    driver.quit()

if __name__ == "__main__":
    main()
