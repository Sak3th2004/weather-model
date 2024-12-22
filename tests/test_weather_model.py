from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Edge()  # This assumes msedgedriver.exe is in PATH


driver.get("file:///C:/Users/gunna/Downloads/weather-model/html/weather_model.html")  # Update this path if needed


print("\nBrowser is now open. Follow these steps:")
print("1. Enter the required values in the form fields.")
print("2. Click the 'Generate Graph' button to see the output graph.")
print("3. When you're done, return to this terminal.\n")


input("Press Enter in this terminal to close the browser and complete the script...")


driver.quit()

print("Browser closed successfully. Test completed.")
