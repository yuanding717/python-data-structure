locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Asia']['China'].append('Beijing')
locations['Africa'] = {'Egypt': ['Cairo']}

usa_sorted = sorted(locations['North America']['USA'])
print usa_sorted

asia_cities = []
for countries, cities in locations['Asia'].iteritems():
    for city in cities:
        city_country = city + " - " + countries
        asia_cities.append(city_country)
print sorted(asia_cities)