import csv

data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

print("Data written to packing_list.csv")

# --- Read the CSV file ---

try:
    with open('packing_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
except FileNotFoundError:
    print("Error: packing_list.csv not found.")
except Exception as e:
    print("Unexpected error while writing CSV:", e)


try:
    with open('packing_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Error: packing_list.csv not found.")
except Exception as e:
    print("Unexpected error while reading CSV:", e)

# --- Seek and read from a specific position ---
try:
    with open('packing_list.csv', 'r') as file:
        file.seek(20)
        content = file.read()
        print("File content after seeking to position 20:")
        print(content)
except FileNotFoundError:
    print("Error: packing_list.csv not found.")
except Exception as e:
    print("Unexpected error while seeking in file:", e)


# --- Basic open test with exception handling ---
try:
    with open('packing_list.csv', 'r') as file:
        pass  # Placeholder
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Unexpected error:", e)