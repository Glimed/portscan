import socket
import termcolor


def scan_port(ipaddress, port):
    """
    Scan a specific port on the given IP address.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        # Attempt to connect to the specified IP address and port
        result = sock.connect_ex((ipaddress, port))
        # Check if the connection was successful
        if result == 0:
            print(termcolor.colored(f"Port {port} is open", "green"))
        else:
            print(termcolor.colored(f"Port {port} is closed", "red"))
    except Exception as e:
        print(termcolor.colored(f"Error: {e}", "yellow"))
    finally:
        # Close the socket
        sock.close()