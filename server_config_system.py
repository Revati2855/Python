server_ip = ("192", "168", "1", "10")

allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed_ips():
    ip = input("Enter IP address to add: ")
    allowed_ips.append(ip)
    print("Allowed IP updated successfully.\n")

def update_server_ip():
    print("Error: server_ip is stored as a tuple and cannot be changed.\n")

def display_configuration():
    print("Server IP:", ".".join(server_ip))
    print("Allowed IPs:")
    for ip in allowed_ips:
        print(ip)
    print()
 
while True:
    print("----- Server Configuration System -----")
    print("1. Add Allowed IP")
    print("2. Change Server IP")
    print("3. Display Configuration")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        update_allowed_ips()
    elif choice == 2:
        update_server_ip()
    elif choice == 3:
        display_configuration()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")