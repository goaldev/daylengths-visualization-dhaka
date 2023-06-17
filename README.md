# Visualizing Daylengths and Solar Noon Times in Dhaka, Bangladesh 

Welcome to the Visualizing Daylengths and Solar Noon Times repository for Dhaka, Bangladesh! 🌞📊

Unleash the power of data visualization as we embark on a journey to explore the daylengths and solar noon times in the vibrant city of Dhaka. By visualizing this valuable information, we gain a clear vision of the abundance of daylight available in this bustling metropolis.

Why is this important, you ask? Well, the length of the day directly impacts various aspects of our lives. Imagine harnessing the longest daylengths to collect sunlight, which serves as the lifeblood of solar panel systems. With this knowledge, we can pave the way for innovative solutions to address the pressing issue of load shedding in Dhaka, Bangladesh.

We scrape data from a reliable source ( https://www.timeanddate.com/sun/bangladesh/dhaka ) and leverage Tableau to create captivating visualizations. 
Dive into our interactive dashboards ( https://public.tableau.com/app/profile/nasrin.akter ) and witness the patterns and dynamics of Dhaka's daylight.

Join us on this illuminating journey and empower yourself with knowledge about daylengths and solar noon times in Dhaka, Bangladesh!


# Build from Sources and Run the Selenium Scraper


1. Clone the repository
```bash
git clone https://github.com/NasrinRipa/mastercourse_scraping_test.git
```
2. Intialize and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads

5. Run the scraper
```bash
python selenium_scraper/scraper.py --chromedriver_path <path_to_chromedriver>
```
6. You will get all the csv files in the csv_files folder and the codes in the selenium_scraper folder. 
