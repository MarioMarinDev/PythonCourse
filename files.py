"""
    r = Read; Shows an error if the file does not exist
    a = Append; Creates the file if it does not exist
    w = Write; Creates the file if it does not exist
    x = Create; Returns an error if the file exists

    file.read() = Read the entire file
    file.read(x) = Read the first 'x' chars of the file
    file.readline = Read the nth line this function is called
    file.readlines = Returns a list of the lines on the file
"""

import os, json

f = open("files/files_01.txt")
print(f.readline())
print(f.readline())
f.close()

# Create a file and then delete it
f = open("files/files_02.txt", "w")
f.close()
if os.path.exists("files/files_02.txt"):
    os.remove("files/files_02.txt")
    print("The file was removed.")
else:
    print("The file does not exist.")

# Create and store data to JSON
my_data = {
    "name": "Mario",
    "age": 25,
    "career": "Software Engineer",
    "hobbies": "Video Games"
}
json_data = json.dumps(my_data, indent=2)
f = open("files/my_data.json", "w")
f.write(json_data)
f.close

# Read a JSON file
f = open("files/my_data.json", "r")
my_read_data = json.loads(f.read())
print(my_read_data["career"])
