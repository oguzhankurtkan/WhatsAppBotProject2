from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver to access WhatsApp Web
driver = webdriver.Chrome()  # If you are using ChromeDriver
driver.maximize_window()
driver.get("https://web.whatsapp.com/")

# Allow time for the user to scan the QR code
print("Please scan the QR code to log in to WhatsApp Web.")
time.sleep(15)  # Adjust the time to allow sufficient time for logging in

def send_whatsapp_message(contact_name, message):
    try:
        # Find the contact search box and enter the contact name
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.clear()
        search_box.send_keys(contact_name)
        search_box.send_keys(Keys.ENTER)
        time.sleep(2)  # Wait for the chat to open

        # Find the message box and type the message
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Message sent to '{contact_name}'.")
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")

# Example usage
if __name__ == "__main__":
    contact = "Reyiz"  # Enter the name of the person you want to send a message to
    msg = "Hello! This is an automated message."
    send_whatsapp_message(contact, msg)
    # You can close the browser after the operation is complete
    time.sleep(5)
    driver.quit()
