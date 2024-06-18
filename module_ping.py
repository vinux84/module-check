import os
from os import system, name


device_dict = {'ROUTER': '254', 'SWITCH 1': '252', 'SWITCH 2': '253', 'WEBRELAY': '240', 'NODE': '102'}

devices_up = {}

devices_down = {}

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def status_display(subnet_ip):
    clear()
    if devices_up:
        print("------Devices that pinged successfully--------\n")
        for device, ip in devices_up.items():
            print(device, "-", f"10.0.{subnet_ip}.{ip}")
        print("")
    if devices_down:    
        print("")
        print("------Devices that pinged unsuccessfully------\n")
        for device, ip in devices_down.items():
            print(device, "-", f"10.0.{subnet_ip}.{ip}")
        print("")

def mod_ping(ip_addr):
    for device, ip in device_dict.items():
        print(f"\n\nPinging {device} now...")
        ping_stat = os.system(f"ping 10.0.{ip_addr}.{ip}")
        if ping_stat:
            devices_down[device] = ip
            print("No Device Found")
        else:
            devices_up[device] = ip
            print("Device Found")
    status_display(ip_addr)

def intro():
    clear()
    print("***Ping Module Test***\n")
    add_subnet = input("Please enter IP subnet for module: ")
    second_switch = input("\nIs there 2 managed switches in this module? [y/n]: ")
    if second_switch == "y":
        mod_ping(add_subnet)
    elif second_switch == "n":
        for device in device_dict.copy():
            if device_dict[device] == '253':
                del device_dict[device]
                mod_ping(add_subnet)
    else:
        print("Please enter Y or N")
        
intro() 
