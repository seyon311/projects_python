country_code = {
    "India": "0091",
    "Australia": "0061",
    "New Zealand": "0064"
}

print("Country code for india is:")
print(country_code.get("India", "Not found"))

print("Country code for Japan is:")
print(country_code.get("Japan", "Not found"))