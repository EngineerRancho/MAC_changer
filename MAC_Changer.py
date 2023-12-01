import subprocess
import os
import optparse

print("                                           ")
print("                     `.-//:://:...         ")       
print("                 `/ymNNNNMNNNNNNNNmo/-`    ")       
print("                :dNMMMMMMMMMMMMMMMMMNNh    ")       
print("               /NMMMMMMMMMMMMMMMMMMMMMN.   ")       
print("              -mMMMMMMMMMMMNNMMMMMMMMMh`   ")       
print("              hMMMNmhsyyysoooshdNMMMMd.    ")       
print("              dMMNy+:--.....--:/oyNMMNo    ")       
print("              sMMm/:-.........--:/hMMMh    ")       
print("              .Nm+/+/::.````-::/++omMM+    ")       
print("               ys:yddddy:``-sddddhs+Nd`    ")       
print("              `/:-/ssd/::..::/ydsy/:d/`    ")       
print("              --...---..-..--.-/-:--//:    ")       
print("              --..`````....--.```..-:/:    ")       
print("              -:..`````.-`.:-````..-:+.    ")       
print("               ``.````.----:-.```..---     ")       
print("                 ```.-::---::::...-.       ")       
print("                 ````.-:--:-::-....`       ")       
print("                  `.....-::-....--`        ")       
print("                  ------------::::-        ")       
print("                 ./--:::///+////://        ")       
print("                  .---------::::::`        ")       
print("                    `....-------.`         ")       
print("                      `.....-..`           ")       
print("                       --.`....            ")       
print("                      .sdhhyhmy.           ")       
print("                        -hMmNo`            ")       
print("                         `dNy              ")       
print("                          hms              ")       
print("                         -NmN.   Pt.Gaurav ")       
print("                         oNdMs    Sharma   ")       
print("                         ydhMm`            ")       
print("                        `ddhNM-            ")       
print("                        .ddddM/        .+` ")   


print(" ")
print(" 1. Ehernet ")
print(" 2. Wifi ")

connection = "wlan0"

network_type = int(input("Network Type : "))

if network_type == 1:
    connection = "eth0"
elif network_type == 2:
    connection = "wlan0"
else:
    print(" Invalid, Select a valid option")
    exit()

new_mac = input("Change the MAC address to : ")


# print("[+] Changing the MAC address to "+ new_mac)
# subprocess.call("sudo su ", shell=True)       #Interupting further program execution
subprocess.call("ifconfig " + connection, shell=True)
subprocess.call("ifconfig " + connection +" down", shell=True)
subprocess.call("ifconfig " + connection +" hw ether "+new_mac, shell=True)
subprocess.call("ifconfig " + connection +" up", shell=True)
subprocess.call("ifconfig " + connection, shell=True)

                # OS MODULE

# os.system('sudo su')
# os.system('ifconfig')
# os.system('ifconfig ' + connection)
# os.system('ifconfig ' + connection + ' down')
# os.system('ifconfig ' + connection + ' hw ether' + new_mac)
# os.system('ifconfig ' + connection + ' up')
# os.system('ifconfig ' + connection)

                # REJECTING EXTRA COMMANDS

# subprocess.call(["ifconfig", connection, "down"])
# subprocess.call(["ifconfig", connection, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", connection, "up"])
# subprocess.call(["ifconfig", connection])

