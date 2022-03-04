import optparse
import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread

def socket_connect(hostname, tcp_port):
	try:
		s_connect = socket.socket(AF_INET, SOCK_STREAM)
		s_connect.connect((hostname, tcp_port))
	except:
		print('[-]Port:' + str(tcp_port) + ' for client:' + hostname+ ' is closed.' )
	else:
		print('[+]Port:'+ str(tcp_port)+ ' for client:' + hostname +' is open.')
		data = 'Hello world\r\n'
		s_connect.send(data.encode(encoding='utf_8'))
		results = s_connect.recv(100)
		print('[+]'+str(results))
		s_connect.close()


def main():
	parser = optparse.OptionParser('-a <hostname/ip-address> -d <port_list_file>')
	parser.usage = '[+]Run: python script.py -a <hostname/ip-address> -d <portlist_file>'
	parser.add_option('-a', dest='hostname', type='string', help='Specify the host IP-address')
	parser.add_option('-d', dest='port_list', type='string', help='Specify port_list file')
	(options, args) = parser.parse_args()
	if (options.hostname == None) | (options.port_list == None):
		print(parser.usage)
		exit()
	else:
		hostname = options.hostname
		port_list = options.port_list
		
		

	try:
		ipof_hostname = socket.gethostbyname(hostname)
		print('The ip-address of "' + hostname + '" is: '+ str(ipof_hostname))
	except socket.gaierror:
		print('Ip address of ' + hostname + ' could not be resolved')
		exit()
		
		
	try:
		port_file = open(port_list)
	except:
		print('[-]Tcp File not found')
		exit()
	else:
		for line in port_file.readlines():
			try:
				tcp_port = int(line.strip('\n'))
			except:
				print('')
				tcp_port = line.strip()
				print('"'+ tcp_port + '"' + ' is an invalid integer, please make correction and try again.')
			else:
				print('')
				print('[*]checking if port:'+ str(tcp_port) + ' is open for client: ' + hostname)
				t = Thread(target=socket_connect, args=(hostname, tcp_port))
				t.start()
				#socket_connect(hostname, tcp_port)
					


if __name__ == '__main__':
	main()
