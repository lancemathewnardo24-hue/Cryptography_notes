# COMMANDS

## Chapter 1 — Linux Basics (Navigation & Files)

### Commands used for system navigation:
- `pwd`                         # Show current directory
- `ls`                          # List files and directories
- `ls -la`                      # List with permissions and hidden files
- `cd <dir>`                    # Change directory
- `cd ..`                       # Go up one directory
- `cd ~`                        # Go to home directory

### Commands used for file management:
- `cp file1 file2`              # Copy files
- `mv old new`                  # Move or rename files
- `rm file`                     # Delete file
- `rm -r dir`                   # Delete directory recursively
- `mkdir dir`                   # Create directory
- `rmdir dir`                   # Remove empty directory

### Commands used for finding files:
- `locate filename`             # Fast file search (database-based)
- `updatedb`                    # Update locate database
- `find /path -name file`       # Search files recursively
- `which command`               # Show command path
- `whereis command`             # Locate binary/source/man files

### Commands used for help:
- `man ls`                      # Manual page
- `ls --help`                   # Command help
- `whoami`                      # Show current user

---

## Chapter 2 — Text Manipulation

### Commands used for viewing files:
- `cat file`                    # Display file contents
- `less file`                   # Scroll through file
- `more file`                   # Basic pager
- `head file`                   # Show first 10 lines
- `tail file`                   # Show last 10 lines
- `tail -f file`                # Live file monitoring

### Commands used for text processing:
- `nl file`                     # Number lines
- `grep "text" file`            # Search text in file
- `grep -i "text" file`         # Case-insensitive search
- `grep -r "text" dir`          # Recursive search
- `sed 's/old/new/' file`       # Find and replace text

### Commands used for redirection & piping:
- `command > file`              # Redirect output
- `command >> file`             # Append output
- `command < file`              # Input redirection
- `command1 | command2`         # Pipe output

---

## Chapter 3 — Network Basics & Analysis

### Commands used for network info:
- `ifconfig`                    # Show network interfaces
- `ip a`                        # Show IP addresses
- `ip link`                     # Show interfaces
- `ip route`                    # Show routing table

### Commands used for wireless networks:
- `iwconfig`                    # Wireless interface info

### Commands used for IP configuration:
- `ifconfig eth0 up`            # Enable interface
- `ifconfig eth0 down`          # Disable interface
- `ifconfig eth0 192.168.1.10`  # Set IP address
- `ifconfig eth0 netmask 255.255.255.0` # Set netmask

### Commands used for MAC & DHCP:
- `ifconfig eth0 hw ether <MAC>`# Change MAC address
- `dhclient eth0`               # Request DHCP lease

### Commands used for DNS:
- `dig google.com`              # DNS lookup
- `cat /etc/resolv.conf`        # View DNS servers

---

## Commands used for scanning:
- `nmap -sn 192.168.68.0/24`    # Host discovery
- `nmap -sV <IP>`               # Service/version scan
- `ip a`                        # Show IP addresses
- `ip route`                    # Show gateway
- `dhclient eth0`               # Renew DHCP lease
