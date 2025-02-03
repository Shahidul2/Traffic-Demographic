# Our Wasted Years (A glimpse into the Traffic Demographic Data of 2024)

## Problem Statement
The goal of this project was to gather worldwide traffic congestion data from [this website](https://www.tomtom.com/traffic-index/ranking/) and find interesting information and instrinsic patterns among the data points. To contemplate on our wasted years on the road, we created a Tableau Dashboard from the scraped data and utilized the following information:

1. What influenced the global traffic rank?
2. Average time needed to travel 10 kilometres in Asia
3. Travel Time improvement and Decline of Countries from 2023
4. Yealy hour lost in road for European Countries

Visit the public dashboard from [here](https://public.tableau.com/app/profile/shahidul.islam5785/viz/2024TrafficDataViz/2024TrafficData)

## Findings from the Dashboard
1. 'Avg travel time for 10km' had high correlation with the 'Rank' while 'Hour lost per year' having slight influence.
2. Philipines was the most congested city in Asia with Saudi Arabia being the least one.
3. In Europe, Romanian people lost most hours on road per year
4. Mauritus had improved their traffin situation the most, meanwhile the situation in Greece plummeted the worst.

## Build from sources
1. Clone the repo
```bash
git clone https://github.com/Shahidul2/Traffic-Demographic.git
```
2. Install and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the scraper
```bash
python scraper.py
```
5. You will have the required 'traffic_index_data.csv' on your local machine.
Else get the file from here: https://github.com/Shahidul2/Traffic-Demographic/blob/main/traffic_index_data.csv

7. Run the data processing notebook for the procesesed CSV file primed for viz.
```bash
pip install jupyter
jupyter nbconvert --execute "Data Processing.ipynb"
```
8. You will get the 'cleaned_traffic_index_data.csv' ready for visualization.
Else get the file from here: https://github.com/Shahidul2/Traffic-Demographic/blob/main/cleaned_traffic_index_data.csv


