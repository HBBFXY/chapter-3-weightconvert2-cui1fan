initial_weight = 60
yearly_gain = 0.5
print("年份\t地球体重(kg)\t月球体重(kg)")
for year in range(1, 11):
    earth_weight = initial_weight + yearly_gain * year
    moon_weight = earth_weight * 0.165
    print("{}\t{:.2f}\t\t{:.2f}".format(year, earth_weight, moon_weight))
