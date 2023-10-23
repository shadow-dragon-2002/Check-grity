import hashlib
import tkinter as tk
from tkinter import filedialog

'''Function which open file explorer to select a files and open which inputs the absolute path of the file into the variable for further processing. The file path is further set into the output fiel variable, and if there was any previous value it gets reset.'''
def browse_file():                          
    file_path = filedialog.askopenfilename()
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)
    return file_path

'''Function which takes the file path from user input and open and reads the file and processes it in chunks then calculate the MD5 and SHA256 Hash values of the file using hashlib and refreshes the variables to input the hash values to the output fields.'''
def Hash():                                 
    file = input_entry.get()
    Buff_Size = 131072                      # Buffer size of 128 kilobytes to process file in chunks for memory efficiency
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(Buff_Size)
            if not data:
                break
            md5_hash.update(data)
            sha256_hash.update(data)
    md5_var.set(md5_hash.hexdigest())
    sha256_var.set(sha256_hash.hexdigest())

'''Function to check the integrity of a file by comparing a user provided hash to the file hash provided by the program and outputs a text label signaling if either of the hashes match or not.'''
def integrity():                            
    user_hash = hash_entry.get().strip()
    md5_hash = md5_var.get().strip()
    sha256_hash = sha256_var.get().strip()
    if str(user_hash) == str(md5_hash):
        result_label.config(text="MD5 hashes match file integrity intact.")
    elif str(user_hash) == str(sha256_hash):
        result_label.config(text="SHA256 hashes match file integrity intact.")
    else:
        result_label.config(text="Hash does not match, file integrity may be compromised.")

# Create the main window and initialize icon
window = tk.Tk()
window.title("Check-grity")

# initialize variable which will carry the hash values to be displayed
md5_var = tk.StringVar()
md5_var.set("")
sha256_var = tk.StringVar()
sha256_var.set("")

# Create widgets
input_label = tk.Label(window, text="Select a File:")
md5_label = tk.Label(window, text="MD5:")
sha256_label = tk.Label(window, text="SHA256:")
input_entry = tk.Entry(window, width=40)
browse_button = tk.Button(window, text="Browse", command=browse_file)
process_button = tk.Button(window, text="Hash File", command=Hash)
output1_entry = tk.Entry(window, state='readonly', textvariable=md5_var, width = 63)
output2_entry = tk.Entry(window, state='readonly', textvariable=sha256_var, width = 63)
hash_label = tk.Label(window, text="Enter Hash to compare:")
hash_entry = tk.Entry(window, width=63)
check_button = tk.Button(window, text="Check Hash", command=integrity)
result_label = tk.Label(window, text="")

# Arrange widgets using the grid layout
input_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_entry.grid(row=0, column=1, padx=10, pady=5)
browse_button.grid(row=0, column=2, padx=10, pady=5)
process_button.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
md5_label.grid(row=2, column=0, padx=10, pady=0, sticky="w")
output1_entry.grid(row=3, column=0, columnspan=8, padx=10, pady=5)
sha256_label.grid(row=4, column=0, padx=10, pady=0, sticky="w")
output2_entry.grid(row=5, column=0, columnspan=8, padx=10, pady=5)
hash_label.grid(row=7, column=0, padx=10, pady=0, sticky="w")
hash_entry.grid(row=8, column=0, columnspan=8, padx=10, pady=5)
check_button.grid(row=9, column=0, columnspan=3, padx=10, pady=5)
result_label.grid(row=10, column=0, columnspan=3, padx=10, pady=5)

# Start the main loop
window.mainloop()
