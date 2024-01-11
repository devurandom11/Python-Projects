# M-MAP

## Description

A Network Scanner made by me, Mike.
M-Map is a Python-based port scanner tool designed to scan specified IP addresses for open ports. This tool was designed by me to learn more about Python and network scanning. There are much more suitable tools for this task such as Nmap, but I wanted to make my own.

## Features

- **IP Address Validation**: Ensures the target IP address is in a correct format.
- **Port Range Specification**: Allows scanning of a specified range of ports.
- **Verbosity Control**: Offers an option for detailed output with debug information.
- **Host Reachability Check**: Verifies if the host is up before scanning.
- **Clean and User-Friendly Interface**: Easy to read output and clear prompts.

## Installation

M-Map requires Python 3 to run. The following Python modules are also required:

- **pyfiglet**: Used for ASCII art text.

Install the required modules with the following command:

```bash
pip install pyfiglet
```

## Usage

Run the script from your command line interface. You have the option to increase verbosity using the `-v` flag. The `-h` flag will display the help menu.

```bash
python m_map.py [-v]
```

After running the script, follow the on-screen prompts to enter the target IP address and the port range you wish to scan.

## Example

```console
    $ python mmap.py
    __   __       __  __
    |  \/  |     |  \/  | __ _ _ __
    | |\/| |_____| |\/| |/ _` | '_ \
    | |  | |_____| |  | | (_| | |_) |
    |_|  |_|     |_|  |_|\__,_| .__/
                              |_|

    Target IP: 192.168.1.1
    Target Port Range <port-port>: 50-80

    Scanning Target: 192.168.1.1
    Scanning Started: 2024-01-10 22:13:48
    --------------------------------------------------

    INFO: [x] 192.168.1.1:53 is open... Happy Hunting!
    INFO: [x] 192.168.1.1:80 is open... Happy Hunting!
    --------------------------------------------------

    Scanning Finished: 2024-01-10 22:14:03

    Open ports: ['192.168.1.1:53', '192.168.1.1:80']
```
