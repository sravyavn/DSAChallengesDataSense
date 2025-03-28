students = [
    {
        'name': 'Aishwarya',
        'semesters': [
            {'Math': 88, 'Science': 91, 'English': 85},
            {'Math': 90, 'Science': 92, 'English': 84}
        ]
    },
    {
        'name': 'Pooja',
        'semesters': [
            {'Math': 79, 'Science': 95, 'English': 88},
            {'Math': 82, 'Science': 81, 'English': 85}
        ]
    },
    {
        'name': 'Sravya',
        'semesters': [
            {'Math': 87, 'Science': 88, 'English': 89},
            {'Math': 91, 'Science': 90, 'English': 93}
        ]
    }
]

result = {}

for i in students:
    name = i['name']
    semesters = i['semesters']
    
    #check if all marks are above 80
    eligible = True
    total_marks = 0

    for j in semesters:
        for subject, marks in j.items():
            if marks <= 80:
                eligible = False  # If any mark is <= 80, student is not eligible
        total_marks += sum(j.values())  # Add marks of the current semester
    
    if eligible:
        result[name] = total_marks

print(result)