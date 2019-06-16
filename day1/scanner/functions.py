from socket import *
from termcolor import colored
from threading import *

actions = ['pscan', 'rscan']

def no_action_picked():
    print("Please select an action: {}" .format(actions))

def on_error():
    print("Enter host and port, run --help for command list")

def port_scanner(host, port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        print(colored(f'[+] port {port}/tcp is open', 'green'))
    except:
        print(colored(f'[-] port {port}/tcp is closed', 'red'))
    finally:
        sock.close()

def range_pscanner(host, startp, endp):
    print(f'Scan results for {host}:')
    for port in range(startp, endp + 1):
        t = Thread(target=port_scanner, args=(host, int(port)))
        t.start()

def no_action_picked():
    print("Please select an action: {}" .format(actions))
