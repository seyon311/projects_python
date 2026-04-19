student_data = {
    "id1" : {"name": "Dave", "class": "V", "subjects": "Maths, English, Science"}, 
    "id2" : {"name": "Jake", "class": "V", "subjects": "Maths, English, Science"},
    "id3" : {"name": "Dave", "class": "V", "subjects": "Maths, English, Science"}, # Duplicate of id1
    "id4" : {"name": "Sara", "class": "V", "subjects": "Maths, English, Science"},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = details["name"], details["class"], details["subjects"]
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

print(result)
