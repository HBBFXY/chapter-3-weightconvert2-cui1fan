initial_weight = 50

annual_increase = 0.5
moon_weight_ratio = 0.165

for year in range(1, 11):
    earth_weight = initial_weight + (annual_increase * year)
    moon_weight = earth_weight * moon_weight_ratio
    print(f"Year {year}: Earth Weight = {earth_weight:.2f}kg, Moon Weight = {moon_weight:.2f}kg")
