import optparse
import socket
from socket import AF_INET, SOCK_STREAM


def socket_connect(hostname, tcp_port):
	try:
		s_connect = socket.socket(AF_INET, SOCK_STREAM)
		s_connect.connect((hostname, tcp_port))
	except:
		print('[-]Port:' + str(tcp_port) + ' for client:' + hostname+ ' is closed.' )
	else:
		print('[+]Port:'+ str(tcp_port)+ ' for client:' + hostname +' is open.')
		data = 'Hellow world\r\n'
		s_connect.send(data.encode(encoding='utf_8'))
		results = s_connect.recv(100)
		print('[+]'+str(results))
		s_connect.close()

def main():
	parser = optparse.OptionParser('-a <hostname/ip-address> -p <tcp_port>')
	parser.usage = '[+]Run: python script.py -a <hostname/ip-address> -p <tcp-port>'
	parser.add_option('-a', dest='hostname', type='string', help='Specify the host IP-address')
	parser.add_option('-p', dest='tcp_port', type='int', help='Specify a tcp port')
	(options, args) = parser.parse_args()
	if (options.hostname == None) | (options.tcp_port == None):
		print(parser.usage)
		exit()
	else:
		hostname= options.hostname
		tcp_port = options.tcp_port

	try:
		ipof_hostname = socket.gethostbyname(hostname)
		print('The ip-address of "' + hostname + '" is: '+ str(ipof_hostname))
	except socket.gaierror:
		print('Ip address of ' + hostname + ' could not be resolved')
		exit()
	print('[*]checking if port:'+ str(tcp_port) + ' is open for client: ' + hostname)
	socket_connect(hostname, tcp_port)


if __name__ == '__main__':
	main()
