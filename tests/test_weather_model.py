from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Microsoft Edge WebDriver
# Ensure that msedgedriver is either in the PATH or provided with the correct path
driver = webdriver.Edge()  # This assumes msedgedriver.exe is in PATH

# Open the HTML file
driver.get("file:///C:/Users/gunna/Downloads/weather-model/html/weather_model.html")  # Update this path if needed

# Inform the user
print("\nBrowser is now open. Follow these steps:")
print("1. Enter the required values in the form fields.")
print("2. Click the 'Generate Graph' button to see the output graph.")
print("3. When you're done, return to this terminal.\n")

# Wait for user input before closing the browser
input("Press Enter in this terminal to close the browser and complete the script...")

# Close the browser
driver.quit()

print("Browser closed successfully. Test completed.")
