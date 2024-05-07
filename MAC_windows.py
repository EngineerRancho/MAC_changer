import subprocess
import random

def change_mac_address(interface, new_mac):
    subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=disable"])
    subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=enable"])
    subprocess.call(["netsh", "interface", "set", "interface", interface, "newmac=" + new_mac])
    print("MAC address of", interface, "changed to", new_mac)

def generate_random_mac():
    random_mac = [0x00, 0x16, 0x3e,
                  random.randint(0x00, 0x7f),
                  random.randint(0x00, 0xff),
                  random.randint(0x00, 0xff)]
    return ':'.join(map(lambda x: "%02x" % x, random_mac))

if __name__ == "__main__":
    print("Select the interface to change MAC address:")
    print("1. Ethernet")
    print("2. Wi-Fi")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        interface = "Ethernet"
    elif choice == "2":
        interface = "Wi-Fi"
    else:
        print("Invalid choice. Please enter 1 or 2.")
        exit()
mac_type = input("Select the MAC mac_type: ")
print("1. Input MAC")
print("2. Random MAC")

if mac_type == 1:
    new_mac = input("Enter the desired MAC address (format: XX:XX:XX:XX:XX:XX): ")
    change_mac_address(interface, new_mac)

elif mac_type ==2:
    new_mac = generate_random_mac()
    print("Generated random MAC address:", new_mac)
    change_mac_address(interface, new_mac)
else:
    print("Select a valid number.")
    exit()