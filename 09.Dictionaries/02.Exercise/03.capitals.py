# Input: list of countries and capitals
countries = input().split(", ")
capitals = input().split(", ")

# Create a dictionary using dictionary comprehension and zip
country_capital_dict = {country: capital for country, capital in zip(countries, capitals)}

# Print each country and its capital
for country, capital in country_capital_dict.items():
    print(f"{country} -> {capital}")
