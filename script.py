from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
import os
import tkinter

import tkinter as tk


options = Options()
#options.set_capability('acceptInsecureCerts', True)
#options.add_argument('--allow-running-insecure-content')
#options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
options.add_argument('--window-size=1920,1080')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep():
    time.sleep(5)



def run_detection_test():
    # Start the Selenium script
    browser = webdriver.Firefox()
    browser.get("http://www.example.com/detection-test")
    
    # Retrieve the result from the Selenium script
    result = browser.find_element(By.ID, 'detectionResult').text
    
    # Update the output field with the result
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.insert("end", result)
    output_field.config(state="disabled")
    
    # Close the browser
    browser.quit()

def convert():
    # Get the value from the input field
    input_value = input_field.get()

    # Create a text file with the input value
    with open("input.txt", "w") as f:
        f.write(input_value)

    # Run a Selenium script to navigate to a website and paste the input
    from selenium import webdriver

    browser = webdriver.Chrome(options=options)
    browser.get("https://quillbot.com/")
    time.sleep(3)
    browser.find_element(By.ID, 'inputText').send_keys(input_value)
    time.sleep(2)
    browser.find_element(By.XPATH, '//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button').click()
    time.sleep(3)
    output = browser.find_element(By.ID, 'outputText')
    converted_value = output.text

    # Update the output field with the converted value
    output_field.config(state="normal")
    output_field.delete("1.0", "end")
    output_field.insert("end", output.text)
    output_field.config(state="disabled")

    with open("input.txt", "w") as f:
        f.write("")



# Create the main window
root = tk.Tk()
root.title("Undetected AI Generated Text")
root.geometry("500x250") # set the size of the window
root.resizable(False, False)

# Create a label for the input field
input_label = tk.Label(root, text="Input", font=("Helvetica", 16))
input_label.pack()

# Create the input field
input_field = tk.Entry(root, width=50) # increase the width of the input field
input_field.pack(pady=10)

# Create a label for the output field
output_label = tk.Label(root, text="Output", font=("Helvetica", 16))
output_label.pack()

# Create the output field
output_field = tk.Text(root, height=5, width=50, state="disabled") # increase the height and width of the output field
output_field.pack(pady=10)

# Create the convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack()

# Start the main event loop
root.mainloop()


