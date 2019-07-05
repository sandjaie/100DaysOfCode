#!/usr/bin/env python3
# Find SSH version on the remote host

from socket import *
from threading import *

def retBanner(ip, port):
    """Returns Open SSH banner of the remote host
    
    Arguments:
        ip [str] -- [IP of the remote host]
        port [int] -- [Port of the remote host]
    
    Returns:
        banner [str] -- [SSH version]
    """
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((ip, port))
        sock.settimeout(3)
        banner = sock.recv(1024).decode()
        sock.close()
        if banner:
            print(f"[+] {ip}:{port}\t{banner}")
    except Exception as err:
        return err
    

def main():
    """Returns banner from remote IP
       Input : IP
    """
    ip = input("Enter IP: ")
    for port in range(10,100):
        t = Thread(target=retBanner, args=(ip, port))
        t.start()
if __name__ == '__main__':
    main()
