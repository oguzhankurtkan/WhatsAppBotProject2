# README

## Automating WhatsApp Messaging Using Selenium

### Overview

This project demonstrates how to use Python's Selenium library to automate sending messages through WhatsApp Web. By leveraging a WebDriver (e.g., ChromeDriver), this script provides a straightforward approach to access WhatsApp Web, search for a contact, and send an automated message.

### Features

1. **Automated Login to WhatsApp Web**: The script allows users to log in by scanning a QR code.
2. **Search for Contacts**: Automates the process of searching for a contact in your WhatsApp contact list.
3. **Send Messages**: Automatically sends a predefined message to the selected contact.
4. **Cross-Browser Compatibility**: Can be adapted for other browsers like Firefox or Edge by changing the WebDriver.

---

### Prerequisites

Before running the project, ensure you have the following installed and set up:

1. **Python**: Version 3.7 or later.
2. **Selenium**: Install Selenium using the following command:
   ```bash
   pip install selenium
   ```
3. **WebDriver**: Install the WebDriver corresponding to your browser version (e.g., ChromeDriver for Google Chrome). Make sure the WebDriver executable is in your system's PATH or the project directory.
4. **WhatsApp Account**: You need an active WhatsApp account linked to your phone.

---

### How It Works

#### 1. **Initialization**
The script initializes the Selenium WebDriver, opens WhatsApp Web, and waits for the user to scan the QR code for authentication.

#### 2. **Search for Contact**
The script locates the search box element on WhatsApp Web using its XPath, enters the contact's name, and opens the chat.

#### 3. **Send Message**
Once the chat is open, the script locates the message box, types the message, and sends it by simulating an Enter key press.

---

### Setup Instructions

1. **Install Dependencies**
   Ensure all required Python libraries are installed:
   ```bash
   pip install selenium
   ```

2. **Download WebDriver**
   Download the appropriate WebDriver for your browser:
   - For Chrome: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
   - For Firefox: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

3. **Clone or Download the Project**
   Clone this repository or download the source code to your local machine.

4. **Run the Script**
   Navigate to the project directory and execute the script:
   ```bash
   python whatsapp_automation.py
   ```

---

### Code Walkthrough

#### 1. **Initialize WebDriver**
The script initializes a WebDriver instance to open WhatsApp Web:
```python
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
```

#### 2. **Wait for QR Code Scan**
The user is given time to scan the QR code for authentication:
```python
print("Please scan the QR code to log in to WhatsApp Web.")
time.sleep(15)
```

#### 3. **Search for Contact**
The script identifies the search box and enters the contact name:
```python
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.clear()
search_box.send_keys(contact_name)
search_box.send_keys(Keys.ENTER)
```

#### 4. **Send Message**
Once the chat is open, the script types and sends the message:
```python
message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
message_box.click()
message_box.send_keys(message)
message_box.send_keys(Keys.ENTER)
```

#### 5. **Close the Browser**
The script terminates the WebDriver session after the operation:
```python
driver.quit()
```

---

### Usage Example

To send a message to a specific contact, modify the variables in the `__main__` section:

```python
if __name__ == "__main__":
    contact = "Name"  # Replace with the recipient's name
    msg = "Hello! This is an automated message."
    send_whatsapp_message(contact, msg)
```

Run the script, and the message will be sent automatically after logging into WhatsApp Web.

---

### Notes

1. **Ensure Stable Internet Connection**: A reliable internet connection is required for WhatsApp Web to work smoothly.
2. **WhatsApp Web Limitations**: The script relies on the current DOM structure of WhatsApp Web. If WhatsApp updates its UI, you may need to adjust the XPath selectors.
3. **Scan the QR Code Every Session**: Due to session expiration, you'll need to scan the QR code each time you run the script.

---

### Troubleshooting

- **Element Not Found**: If an element cannot be located, check the XPath and update it if WhatsApp has modified its DOM structure.
- **WebDriver Compatibility Issues**: Ensure the WebDriver version matches your browser version.
- **Session Timeout**: If the QR code scan times out, restart the script and scan again.

---

### Future Enhancements

1. **Dynamic Contact Selection**: Allow users to input contact names dynamically.
2. **Bulk Messaging**: Extend functionality to send messages to multiple contacts in a loop.
3. **Media Sharing**: Add support for sending images, videos, or documents.
4. **Error Handling**: Improve error handling for network issues or element detection failures.

---

### License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code with proper attribution.

---

### Author

Developed by Oğuzhan Kurtkan.

For inquiries or support, feel free to reach out via email at oguzhankurtkan@gmail.com

https://www.youtube.com/watch?v=j8hrai6KY3s
