import tkinter as tk

def main():
    # Create the main window
    window = tk.Tk()
    window.title("File Uploader")

    # Create a label and entry for the file name
    file_name_label = tk.Label(window, text="Enter the file name to upload:")
    file_name_label.pack()
    file_name_entry = tk.Entry(window)
    file_name_entry.pack()

    # Create a label and entry for the S3 bucket
    bucket_label = tk.Label(window, text="Enter the name of the S3 bucket:")
    bucket_label.pack()
    bucket_entry = tk.Entry(window)
    bucket_entry.pack()

    # Create a label and entry for the content type
    content_type_label = tk.Label(window, text="Enter the content type of the file:")
    content_type_label.pack()
    content_type_entry = tk.Entry(window)
    content_type_entry.pack()

    # Create a label and entry for the profile name
    profile_label = tk.Label(window, text="Enter the profile name:")
    profile_label.pack()
    profile_entry = tk.Entry(window)
    profile_entry.pack()

    # Create a label and entry for the endpoint URL
    endpoint_url_label = tk.Label(window, text="Enter the endpoint url:")
    endpoint_url_label.pack()
    endpoint_url_entry = tk.Entry(window)
    endpoint_url_entry.pack()

    # Create a label and entry for the region
    region_label = tk.Label(window, text="Enter the region:")
    region_label.pack()
    region_entry = tk.Entry(window)
    region_entry.pack()

    # Create a label and entry for the cloud provider
