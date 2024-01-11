import socket
import sys
from datetime import datetime
import os
import logging
import pyfiglet

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# Function to clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Function to validate IP address
def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


# Function to validate port range
def validate_ports(ports):
    try:
        start_port, end_port = map(int, ports.split("-"))
        return (
            0 <= start_port < 65536 and 0 <= end_port < 65536 and start_port < end_port
        )
    except ValueError:
        return False


def print_banner():
    ascii_banner = pyfiglet.figlet_format("M-Map")
    print(ascii_banner)


def get_ip():
    while True:
        target = input("Target IP: ")
        if validate_ip(target):
            break
        print("Invalid IP address. Please try again.")
    return target


def get_ports():
    while True:
        ports = input("Target Port Range <port-port>: ")
        if validate_ports(ports):
            break
        print("Invalid port range. Please try again.")
    return ports


def print_start(target):
    print(f"Scanning Target: {target}")
    print(f"Scanning Started: {datetime.now()}")
    print("-" * 50)


def scan(target, ports):
    open_ports = []
    start_port, end_port = map(int, ports.split("-"))
    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as t_socket:
                t_socket.settimeout(0.5)
                result = t_socket.connect_ex((target, port))
                if result == 0:
                    print(f"[x] {target}:{port} is open... Happy Hunting!")
                    open_ports.append(f"{target}:{port}")
                else:
                    print(f"[-] {target}:{port} is closed...")
    except KeyboardInterrupt:
        print("\n[!] User Interrupt")
        sys.exit()
    except socket.error:
        print("\n[!] Host not responding :/")
        sys.exit()

    return open_ports


def print_results(results):
    print("-" * 50)
    print(f"Scanning Finished: {datetime.now()}")
    if len(results) > 0:
        print(f"\nOpen ports: {results}")
    else:
        print("\nNo open ports found :(")


def main():
    clear_screen()
    print_banner()
    target = get_ip()
    ports = get_ports()
    print_start(target)
    results = scan(target, ports)
    print_results(results)


if __name__ == "__main__":
    main()
