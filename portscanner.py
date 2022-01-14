import socket
import termcolor

def scan(target, ports):
	print(termcolor.colored(('\n' + 'Starting Scan for: ' + target), 'green'))
	for port in range(1, ports):
		scan_port(targets, port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened at " + str(port))
		sock.close()
	except:
		pass

targets = input("[*] Enter Target To Scan (split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' ', ports))
else:
	scan(targets, ports)
