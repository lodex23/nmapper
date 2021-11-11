import os

os.system('clear')


ip = input("Enter Target ip(Ctrl + c to exit): ")
os.system('clear')
print("-----------------------------")
print("Target Ip set to: " + ip)
print("-----------------------------")

os.system('clear')



def Function_IP_protocol(host):
    os.system('nmap -sO ' + host)
    input("Press enter to go back")
    os.system('nmapper')


def Function_Service_Version(host):
    os.system('nmap -sV ' + host)
    input("Press enter to go back")
    os.system('nmapper') 

def Function_All_Hosts(host):
    os.system('nmap -sV ' + host + ' -Pn')
    os.system("Press enter to go back")
    os.system('nmapper')


def Function_Exit():
	os.system('exit')




print("Ip: " + ip)
print("--------------------------------")
print("Choose option")
print("--------------------------------")
print("1) Ip Protocol")
print("2) Service/Version")
print("3) All Hosts (slow)")
print("4) Exit")
print("--------------------------------")

oP = input("Choose option: ")


os.system('clear')



if oP == "1":
    Function_IP_protocol(ip)

elif oP == "2":
    Function_Service_Version(ip)

elif oP == "3":
    Function_All_Hosts(ip)

elif oP == "4":
    Function_Exit()

else:
    print("This Number is invalid.")

    

    
