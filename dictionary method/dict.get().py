car_prices = {
    "BMW": 20000,
    "FORD": 30000,
    "ISUZU": 45000
}

price_of_BMW = car_prices.get("BMW")
print("Price of BMW:", price_of_BMW)
price_of_FORD = car_prices.get("FORD")
print("price of FORD :", price_of_FORD)
price_of_truck = car_prices.get("truck", "Not available")
print("Price of truck:", price_of_truck)
