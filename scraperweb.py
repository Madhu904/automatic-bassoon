import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.accuweather.com/"


response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')

    
    temperature = soup.find("div", class_="display-temp").text
    humidity = soup.find("span", class_="value").text

    
    weather_data = [
        {"Temperature": temperature, "Humidity": humidity}
    ]

   
    csv_file = "weather_data.csv"

    
    with open(csv_file, mode='w', newline='') as file:
        fieldnames = ["Temperature", "Humidity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        
        writer.writeheader()
        
       
        writer.writerows(weather_data)

    print("Weather data saved to", csv_file)

else:
    print("Failed to retrieve data from the website. Status code:", response.status_code)