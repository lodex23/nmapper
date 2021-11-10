import os

ip = input("Enter Target ip: ")
os.system('clear')
print("-----------------------------")
print("Target Ip set to: " + ip)
print("-----------------------------")
input("Press enter to start scan")


os.system('clear')
os.system('nmap -sV ' + ip + ' -o nmap_result.txt')
print("-----------------------------")
input("Scane done: Press Enter to show Results")


print("-----------------------------")
print("nmap_result.txt")
