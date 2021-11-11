import os

ip = input("Enter Target ip: ")
os.system('clear')
print("-----------------------------")
print("Target Ip set to: " + ip)
print("-----------------------------")

os.system('clear')



def Function_IP_protocol(host):
    os.system('nmap -sO ' + host)


def Function_Service_Version(host):
    os.system('nmap -sV ' + host)


def Function_All_Hosts(host):
    os.system('nmap -sO ' + host + ' -Pn')



print("--------------------------------")
print("Choose option")
print("--------------------------------")
print("1) Ip Protocol")
print("2) Service/Version")
print("3) All Hosts")
print("--------------------------------")

oP = input("Choose option: ")


if oP == 1:
    Function_IP_protocol(ip)

elif oP == 2:
    Function_Service_Version(ip)

elif oP == 3:
    Function_All_Hosts(ip)

else:
    print("This Number is invalid.")

    
