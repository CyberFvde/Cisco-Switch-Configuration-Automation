import requests
import tkinter as tk

# Define the GUI window
root = tk.Tk()
root.title("Cisco Switch Configuration")

# Define the API key and URL text fields
api_key_label = tk.Label(root, text="API Key:")
api_key_label.grid(row=0, column=0)

api_key_entry = tk.Entry(root)
api_key_entry.grid(row=0, column=1)

url_label = tk.Label(root, text="URL:")
url_label.grid(row=1, column=0)

url_entry = tk.Entry(root)
url_entry.grid(row=1, column=1)

# Define the interface configuration fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=2, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=2, column=1)

desc_label = tk.Label(root, text="Description:")
desc_label.grid(row=3, column=0)

desc_entry = tk.Entry(root)
desc_entry.grid(row=3, column=1)

ip_label = tk.Label(root, text="IP Address:")
ip_label.grid(row=4, column=0)

ip_entry = tk.Entry(root)
ip_entry.grid(row=4, column=1)

mask_label = tk.Label(root, text="Netmask:")
mask_label.grid(row=5, column=0)

mask_entry = tk.Entry(root)
mask_entry.grid(row=5, column=1)

# Define the update interface button
def update_interface():
    # Get the API key and URL from the text fields
    api_key = api_key_entry.get()
    url = url_entry.get()

    # Get the interface configuration details from the text fields
    name = name_entry.get()
    desc = desc_entry.get()
    ip = ip_entry.get()
    mask = mask_entry.get()

    # Define the headers for the HTTP request
    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
        "Authorization": f"Bearer {api_key}"
    }

    # Define the data payload for the HTTP request
    data = {
        "ietf-interfaces:interface": {
            "name": name,
            "description": desc,
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": ip,
                        "netmask": mask
                    }
                ]
            }
        }
    }

    # Send the HTTP request to update the Cisco switch interface configuration
    response = requests.patch(url, json=data, headers=headers)

    # Check the response status code to see if the request was successful
    if response.status_code == 200:
        result_label.config(text="Interface configuration updated successfully")
    else:
        result_label.config(text=f"Error updating interface configuration: {response.text}")

update_button = tk.Button(root, text="Update Interface", command=update_interface)
update_button.grid(row=6, column=1)

# Define the result label
result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2)

# Run the GUI loop
root.mainloop()
