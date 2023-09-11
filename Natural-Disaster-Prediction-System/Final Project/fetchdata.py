from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import csv

# Start a new browser session
browser = webdriver.Chrome('/path/to/chromedriver')  # replace with the path to your ChromeDriver
browser.get('http://aws.imd.gov.in:8091')

# Choose "Daily Rainfall" from the options (modify the selector if it doesn't work)
# This is a placeholder; you might need to adjust the selector based on the exact HTML structure.
daily_rainfall = browser.find_element_by_id('id_of_daily_rainfall_option')
daily_rainfall.click()

# Select "all_state" from dropdown (modify the selector if it doesn't work)
all_states = Select(browser.find_element_by_id('id_of_states_dropdown'))
all_states.select_by_visible_text('all_state')

# Select all available dates. This is a placeholder and might need modification.
dates = Select(browser.find_element_by_id('id_of_date_dropdown'))
for date in dates.options:
    date.click()

# Click the "view" button to generate the table (modify the selector if it doesn't work)
view_button = browser.find_element_by_id('id_of_view_button')
view_button.click()

# Wait for some time to let the table load
time.sleep(10)

# Now, fetch the table data
table = browser.find_element_by_id('id_of_the_table')  # modify the selector if it doesn't work
rows = table.find_elements_by_tag_name('tr')

# Save the table data to a CSV file
with open('rainfall_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        csv_row = [cell.text for cell in row.find_elements_by_tag_name('td')]
        writer.writerow(csv_row)

# Close the browser session
browser.quit()
