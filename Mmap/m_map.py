import argparse
import socket
import sys
from datetime import datetime
import os
import logging
import pyfiglet
import subprocess
import platform


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def set_logging():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Increase output verbosity"
    )
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def print_banner():
    ascii_banner = pyfiglet.figlet_format("M-Map")
    print(f"\n{ascii_banner}")


def print_start(target):
    print(f"\nScanning Target: {target}")
    print(f"\nScanning Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)


def print_results(results):
    print("-" * 50)
    print(f"Scanning Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if len(results) > 0:
        print(f"\nOpen ports: {results}\n")
    else:
        print("\nNo open ports found :(\n")


def get_ip():
    while True:
        target = input("Target IP: ")
        if validate_ip(target):
            break
        print("Invalid IP address. Please try again.")
    return target


def validate_ip(ip):
    try:
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return response.returncode == 0


def get_ports():
    while True:
        ports = input("Target Port Range <port-port>: ")
        if validate_ports(ports):
            break
        print("Invalid port range. Please try again.")
    return ports


def validate_ports(ports):
    try:
        start_port, end_port = map(int, ports.split("-"))
        return (
            0 <= start_port < 65536 and 0 <= end_port < 65536 and start_port < end_port
        )
    except ValueError:
        return False


def scan(target, ports):
    open_ports = []
    start_port, end_port = map(int, ports.split("-"))
    if not ping_host(target):
        print("\n[!] Host is not responding :/\n")
        sys.exit()
    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as t_socket:
                t_socket.settimeout(0.5)
                result = t_socket.connect_ex((target, port))
                if result == 0:
                    logging.info(f"[x] {target}:{port} is open... Happy Hunting!")
                    open_ports.append(f"{target}:{port}")
                else:
                    logging.debug(f"[-] {target}:{port} is closed...")
    except KeyboardInterrupt:
        print("\n[!] User Interrupt")
        sys.exit()
    except socket.error:
        print("\n[!] Host not responding :/\n")
        sys.exit()

    return open_ports


def main():
    set_logging()
    clear_screen()
    print_banner()
    target = get_ip()
    ports = get_ports()
    print_start(target)
    results = scan(target, ports)
    print_results(results)


if __name__ == "__main__":
    main()
