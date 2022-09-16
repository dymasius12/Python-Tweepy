import sys 
# We are going to save the clipboard in json file
import json

# below print the after the python file name
# print(sys.argv)

#this is a variable where you want to save your data
SAVED_DATA = "tweets.json"

# Make a file that can create JSON file for us
def save_data(filepath, data):
    with open(filepath, "a") as f:
        json.dump(data, f)

def load_data(filepath):
    #check if the file exist or not
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# save_data("test.json", {"key": "value"})

# if len(sys.argv) == 2:
#     command = sys.argv[1]
    
#     data = load_data(SAVED_DATA)

#     # Basically inputing the value key to the json file
#     if command == "save":
#         key = input("enter a key: ")
#         data[key] = clipboard.paste()
#         save_data(SAVED_DATA,data)
#         print("data is saved!")

#     elif command == "load":

#         #ask the key and make sure it exists!
#         key = input("Enter a key: ")
#         if key in data: 
#             clipboard.copy(data[key])
#             print("Data is copied into the clipboard!")
#         else:
#             print("Key does not exist!")

#     elif command =="list":
#         print(data)
#     else:
#         print("Unknown command!")

# else:
#     print("Please type in only 1 command.")