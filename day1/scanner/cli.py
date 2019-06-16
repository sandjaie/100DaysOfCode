import click
from functions import *


def pscan(host, ports):
    """This function scans a port against a host
    
    Arguments:\n
        host -- 'Host IP'\n
        port -- 'Port Number'
    """
    for port in ports.split(','):
        try:
            print(f'Scan results for {host}:')
            portScanner(host, int(port))
        except:
            on_error()

def rscan(host, startp, endp):
    """This scans a range of ports against the host
    
    Arguments: \n
        host -- 'Host IP Address' \n
        startp -- 'Start Port' \n
        endp -- 'End Port'
    """
    try:
        #print(f'Scan results for {host}:')
        rangePortScanner(host, int(startp), int(endp))
    except:
        on_error()


@click.command()
@click.argument('action')
@click.option('--host', '-h', help='Enter host address e.g -h 192.168.100.1')
@click.option('--ports', '-p', help='Enter port number e.g -p 80,22,8080')
@click.option('--startp', '-sp', help='Enter the range of ports e.g --startp 80 --endp 100')
@click.option('--endp', '-ep', help='Enter the range of ports e.g --startp 80 --endp 100')
def main(action, host, ports, startp, endp):
    """
    Select an action pscan|rscan
    """
    action_dict = {
        'pscan' : lambda : pscan(host=host, ports=ports),
        'rscan' : lambda : rscan(host=host, startp=startp, endp=endp)
    }
    def default():
        no_action_picked()
    
    action_run = action_dict.get(action, default)
    action_run()

if __name__ == '__main__':
    main()
