from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random


# Set up the Chrome driver service
service = Service(executable_path="chromedriver.exe")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Open the website and maximize the window
driver.get('http://tutorialsninja.com/demo/')
driver.maximize_window()

# Wait until the "Phones & PDAs" link is clickable and click it
phones = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Phones & PDAs"]')))
phones.click()

# Wait until the "iPhone" link is clickable and click it
iphone = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="iPhone"]')))
iphone.click()
time.sleep(1)

# Wait until the first image thumbnail is clickable and click it
first_pic = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="thumbnails"]/li[1]')))
first_pic.click()
time.sleep(2)

# Navigate through images
next_click = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@title="Next (Right arrow key)"]')))
for i in range(5):
    next_click.click()
    time.sleep(2)
    
# Save a screenshot
driver.save_screenshot('phoneScreenshot#' + str(random.randint(0, 101)) + '.png')

 # Close the image view
x_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@title="Close (Esc)"]')))
x_button.click()
time.sleep(1)

# Change the quantity of the product
quantity = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, 'input-quantity')))
quantity.click()
time.sleep(1)
quantity.clear()
time.sleep(1)
quantity.send_keys('3')
time.sleep(1)

# Add the product to the cart
add_to_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'button-cart')))
add_to_button.click()
time.sleep(2)


# Wait until the "Tablets" link is clickable and click it
tablets = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Tablets"]')))
tablets.click()

# Wait until the "Tablet" link is clickable and click it
samsung = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[text()="Samsung Galaxy Tab 10.1"]')))
samsung.click()
time.sleep(1)

# Wait until the first image thumbnail is clickable and click it
first_pic = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//ul[@class="thumbnails"]/li[1]')))
first_pic.click()
time.sleep(2)

# Navigate through images
next_click = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@title="Next (Right arrow key)"]')))
for i in range(6):
    next_click.click()
    time.sleep(2)
    
# Save a screenshot
driver.save_screenshot('TabletScreenshot#' + str(random.randint(0, 101)) + '.png')

# Close the image view
x_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@title="Close (Esc)"]')))
x_button.click()
time.sleep(1)

# Change the quantity of the camera
quantity = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, 'input-quantity')))
quantity.click()
time.sleep(1)
quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)


# Add the product to the cart
add_to_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'button-cart')))
add_to_button.click()
time.sleep(2)

# Go to the cart and proceed to checkout
go_to_cart = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, 'cart-total')))
go_to_cart.click()
time.sleep(1)

checkout = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//p[@class="text-right"]/a[2]')))
checkout.click()
time.sleep(10)



