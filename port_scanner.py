import socket

def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ").strip()
    ports = range(20, 1025)  # Common ports
    scan_ports(target, ports)
