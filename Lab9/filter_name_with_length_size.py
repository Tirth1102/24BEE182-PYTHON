faculty_names = ['Dr. Johnson', 'Alexander', 'Kim', 'Catherine', 'Christopher', 'Joe']

long_names = list(filter(lambda name: len(name) > 8, faculty_names))
print("Names longer than 8 characters:", long_names)

# Output:
# Names longer than 8 characters: ['Dr. Johnson', 'Alexander', 'Catherine', 'Christopher']
