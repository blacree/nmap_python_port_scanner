import optparse
import socket
import nmap
# import pdb
import sys

""" All information you need to know of your target client. This can be printed using: 
print(nmapscan[ip_address]) after you have made use of the nmap.scan() function."""

def nmapscanner(ip_address, port):
	try:
		nmapscan = nmap.PortScanner()
		nmapscan.scan(ip_address, port)
		state=nmapscan[ip_address]['tcp'][int(port)]['state']
		print('[+]'+ ip_address + ' tcp/' + str(port) + ' is ' + state)
		#pdb.set_trace()
		hostnames= nmapscan[ip_address]['hostnames'][0]['name']
		typee = nmapscan[ip_address]['hostnames'][0]['type']
		macaddress = nmapscan[ip_address]['addresses']['mac']
		ipv4 = nmapscan[ip_address]['addresses']['ipv4']
		vendor = nmapscan[ip_address]['vendor'][macaddress]
		target_state = nmapscan[ip_address]['status']['state']
		state_reason = nmapscan[ip_address]['status']['reason']
		port_state = nmapscan[ip_address]['tcp'][int(port)]['state']
		port_reason = nmapscan[ip_address]['tcp'][int(port)]['reason']
		port_name = nmapscan[ip_address]['tcp'][int(port)]['name']
		service_product = nmapscan[ip_address]['tcp'][int(port)]['product']
		product_version = nmapscan[ip_address]['tcp'][int(port)]['version']
		extrainfo = nmapscan[ip_address]['tcp'][int(port)]['extrainfo']
		cpe = nmapscan[ip_address]['tcp'][int(port)]['cpe']
		print('[+]ipv4_address:' + ipv4 + '. Mac_address:' + macaddress)
		print('[+]Vendor: ' + vendor)
		print('[+]Target_state:' + target_state + '   Reason:' + state_reason)
		print('[+]Port_state(' + str(port) + '):' + port_state + '   Reason:' + port_reason)
		print('[+]Port_name:'+ port_name + '   service_prodcut:' + service_product )
		print('[+]Product_version:' + product_version + '   Extrainfo:'+ extrainfo )
		print('[+]CPE: ' + cpe + '.')
	except:
		print('[-]Error during scanning. Exiting...')


def main():
	print(sys.argv)
	parser = optparse.OptionParser('-a <hostname/hostname> -p <port>')
	parser.add_option('-a', type='string', dest='ipaddress', help='Enter a valid ip-address')
	parser.add_option('-p', type='string', dest='port', help='Enter a port number')
	parser.usage = '[*]Run: python script.py -a <hostname(domain)/ipaddress> -p <port>'
	(options, args) = parser.parse_args()
	if (options.ipaddress == None ) or (options.port == None):
		print(parser.usage)
		exit()
	else:
		hostaddress = options.ipaddress
		port = options.port
	ip_address = ''
	# Retrieve the ip-address, if a domain name was passed to script
	try:
		ip_address = socket.gethostbyname(hostaddress)
	except:
		print('Cannot resolve ip-address for '+ hostaddress)
		exit()
	else:
		print('The ip-address of "' + hostaddress + '" is: '+ str(ip_address))
	nmapscanner(ip_address, port)
	
		
if __name__ == '__main__':
	main()
