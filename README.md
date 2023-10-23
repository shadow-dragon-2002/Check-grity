# Check-grity

A simple Python program with GUI to check and compare file hashes. Currently supports MD5 and SHA256 hashes. This program can be used to do basic integrity checks or to verify files which have been edited.

### GUI:

![GUI](https://github.com/shadow-dragon-2002/Check-grity/blob/main/Check-grity_GUI.png?raw=true)

### How to use :

* Using CLI copy and paste the following command into the terminal or click the download zip button to clone the repository.

  `git clone https://github.com/shadow-dragon-2002/Check-grity.git`

* Change the directory to the cloned repository.
  
  `cd Check-grity`

* Execute the script using Python.
  
  `python3 Check-grity`

### How it works:

This particular Python program lets you choose a file via file explorer of the OS and extract its hash values using hashlib. There is also an option for the user to manually enter a hash and compare it to the extracted hashes, the program lets you know if the manually entered hash matches the extracted hashes or not.
