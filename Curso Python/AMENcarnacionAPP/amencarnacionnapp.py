import tkinter as tk
import requests
from bs4 import BeautifulSoup

def fetch_video_links():
    url = url_entry.get()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        video_links = [video['src'] for video in soup.find_all('video')]
        result_text.delete(1.0, tk.END)  # Clear previous results
        for link in video_links:
            result_text.insert(tk.END, link + '\n')
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Video Link Extractor")

# URL entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Fetch button
fetch_button = tk.Button(root, text="Fetch Video Links", command=fetch_video_links)
fetch_button.pack()

# Result text area
result_text = tk.Text(root, height=15, width=50)
result_text.pack()

# Start the GUI event loop
root.mainloop()