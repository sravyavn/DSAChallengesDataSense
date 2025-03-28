#Day13Q26:  Deep Nested List + Comprehension + Filtering by Condition 
cities = [
    {
        'name': 'Mumbai',
        'areas': {
            'Andheri': [32, 33, 31, 30, 29, 34, 35],
            'Bandra': [31, 32, 30, 30, 31, 33, 34],
        }
    },
    {
        'name': 'Delhi',
        'areas': {
            'Rohini': [28, 29, 27, 30, 31, 32, 29],
            'Saket': [33, 35, 36, 34, 33, 32, 31],
        }
    },
    {
        'name': 'Chennai',
        'areas': {
            'T Nagar': [34, 35, 36, 37, 34, 35, 33],
            'Velachery': [32, 31, 33, 34, 32, 30, 31]
        }
    }
]

hot_cities = [] 

for city in cities:
    above_30 = True  

    for area, temps in city['areas'].items():
        avg_temp = sum(temps) / len(temps) 
        if avg_temp <= 30:
            above_30 = False
            break  

    if above_30:
        hot_cities.append(city['name'])

print(hot_cities)