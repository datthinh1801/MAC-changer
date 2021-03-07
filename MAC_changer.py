#! /bin/python3

import argparse
import re
import subprocess


def change_mac(interface, new_mac):
    """Change the MAC address of the specified interface."""
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.run(["sudo", "ifconfig", interface, "down"])
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["sudo", "ifconfig", interface, "up"])


def parse_arguments():
    """Get user input and parse arguments."""
    # Create an  ArgumentParser object
    parser = argparse.ArgumentParser(prog="MAC changer")

    # Add arguments to the object
    parser.add_argument("-i", "--interface", nargs='?', dest="interface", required=True,
                        help="the interface to be changed MAC address")
    parser.add_argument("-m", "--mac", nargs='?', dest="new_mac", required=True,
                        help="new mac address")

    # Parse user inputs and return it as an object storing those inputs
    return parser.parse_args()


def verify(interface, mac):
    """Verify operation"""
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    if (re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result)).group(0)) == mac:
        print(f"[+] {interface} is changed to {mac} successfully!")
    else:
        print(f"[-] Cannot change the MAC address of {interface}.")


# Main routine
args = parse_arguments()
change_mac(args.interface, args.new_mac)
verify(args.interface, args.new_mac)
