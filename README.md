Note: It is illegal to scan a computer not owned by you, unless given explicit permission to do so.


# nmap_python_port_scanner
The python script helps to scan the port of a target, return the port status and much more.
Nmap scanner is a very powerful scanner. It returns comprehensively almost all information you need to know of your target client. It also has the ability to determine if a port is being filtered by a firewall of which it returns the port status as filtered; and much more features.

#nmapscanner.py
The nmapscanner.py helps to show you all the dictionary fields returned by nmap when you perform a scan on a target. It also shows you how to extract and query each dictionary field, priting the contained information in whatever way you choose.

#nmapscanner2.py
The python script actually puts the information in nmapscanner.py into use by extracting the valuable information wanted about the target and printing them to screen.

#socketscanner.py
This python script performs port scanning but using the socket python package instead.

#socketscanner_dict.py
This python script also makes use of the socket python package, but it takes a port_list file containing list of ports it would scan against the target machine.

Note: The socket package scanning has being tested to return more reliable result in port scanning than the python-nmap package. It's best you use the linux nmap utility to get the best from nmap scanning.
