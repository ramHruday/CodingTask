import csv
import datetime
import api_service
from config_api import COFFEE
from csv_service import write_to_csv
import coffee

coffeeApi = api_service.ApiService(COFFEE["base_url"])

iced = coffee.CoffeeDeserializer().read("output/2022-10-05T23꞉14꞉06-05꞉00_-_iced.json")
hot = coffeeApi.get(COFFEE["endpoint"])

write_to_csv(iced, hot)
