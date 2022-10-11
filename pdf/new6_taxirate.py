'''6) create function that calculate & return total taxi fare base upon given price per km and km of travel. if km is above 20 then 5% discount should be given taxi fare 
'''

# fuelprice=int(input("enter a fuel price per liter"))
# km=int(input("enter a km "))
# mileage_fuel_consumption=km/fuelprice
# if km>20:
#     discount=mileage_fuel_consumption/5
#     perkm=fuelprice/discount
# else:
#     perkm=fuelprice/mileage_fuel_consumption
#     print(perkm)

def taxirate(travel_km,price_per_km):
    if travel_km>20:
        discount=price_per_km/5
        price_per_km=price_per_km-discount
        total_price=travel_km*price_per_km
        print(round(total_price))
    else:
        total_price=travel_km*price_per_km
        print(total_price)
    

travel_km=int(input("enter a travel km : "))
price_per_km=int(input("per km price : "))
taxirate(travel_km,price_per_km)