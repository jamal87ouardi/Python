import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO





def on_select(event):
    selected_value = combo_box.get()
    selected_index=combo_box.current()
    model=data[selected_index]["model"]
    label.config(text=f"model: {model}")
    url=data[selected_index]["image"]
    print(url)

    response = requests.get(url)
    
    if response.status_code == 200:
        # Open the image using Pillow
        img = Image.open(BytesIO(response.content))

        resized = img.resize((200, 200))
        
        # Convert the image to a PhotoImage object
        img = ImageTk.PhotoImage(resized)
        
        # Display the image in a Label widget
        image_label.config(image=img)
        image_label.image = img  # Keep a reference to prevent garbage collection
    else:
        #display error msg
        print("erruer: ",response.status_code)



# Create a tkinter window
window = tk.Tk()
window.geometry("400x400")
window.title("Dropdown Example")

# Create a label
label = tk.Label(window, text="Select an option:")
label.pack(pady=10)



import requests

# Define the API endpoint URL
api_url = 'https://run.mocky.io/v3/9ca73e9c-b75e-473e-9853-15d727be4c4b'

# Make a GET request to the API
response = requests.get(api_url)

data=[]
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Now you can work with the data as a Python dictionary
    # For example, let's print the contents of the 'data' key
    print(data[0]["make"])

    listMakes=[]

    for i in range(len(data)):
        listMakes.append(data[i]["make"])

    combo_box = ttk.Combobox(window, values=listMakes)
    combo_box.pack(pady=10)
    combo_box.bind("<<ComboboxSelected>>", on_select)

else:
    # If the request was not successful, print an error message
    print(f"Failed to fetch data. Status code: {response.status_code}")


# Create a combobox


# Set a default value for the combobox
#combo_box.set("Option 1")

# Bind a function to the combobox selection event

image_label = tk.Label(window, width=150, height=150)

image_label.pack(pady=10)

# Start the Tkinter main loop
window.mainloop()
