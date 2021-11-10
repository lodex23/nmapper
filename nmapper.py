import os

ip = input("Enter Target ip: ")
os.system('clear')
print("-----------------------------")
print("Target Ip set to: " + ip)
print("-----------------------------")
input("Press enter to start scan")


os.system('clear')
os.system('nmap -sV ' + ip)
