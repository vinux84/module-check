import os
import time
from os import system, name

device_dict = {'ROUTER': '254', 'SWITCH 1': '252', 'SWITCH 2': '253', 'WEBRELAY': '240', 'NODE': '101'}

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
        os.system(f"ping 10.0.{ip_addr}.{ip} > ping.txt")
        with open('ping.txt', 'r') as file:
            data = file.read()
            if "TTL" in data:
                print(f'\n{device} up...')
                devices_up[device] = ip
            else:
                print(f'\n{device} down...')
                devices_down[device] = ip
    status_display(ip_addr)

def intro():
    clear()
    print("***Ping Module Test***\n")
    add_subnet = input("Please enter IP subnet for module: ")
    second_switch = input("\nIs there 2 managed switches in this module? [y/n]: ")
    if second_switch == "y":
        pass
    elif second_switch == "n":
        for device in device_dict.copy():
            if device_dict[device] == '253':
                del device_dict[device]  
    else:
        print("Please enter Y or N")
    
    which_node = input("\nDoes this have a Orin Node? [y/n]: ")
    if which_node == "y":
        for device, ip in device_dict.items():
            if device == 'NODE':
                device_dict[device] = '102'
    elif which_node == "n":
        pass
    else:
        print("Please enter Y or N")
    
    mod_ping(add_subnet)
    
intro() 
