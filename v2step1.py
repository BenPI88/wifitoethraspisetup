import os
dhcpcd = open("/etc/dhcpcd.conf","a")
dhcpcd.write("denyinterfaces eth0")
dhcpcd.close()
interfaces = open("sudo nano /etc/network/interfaces", "a")
interfaces.write("auto eth0")
interfaces.write("allow-hotplug eth0")
interfaces.write("iface eth0 inet static")
interfaces.write("    address 192.168.1.1")
interfaces.write("    netmask 255.255.255.0")
interfaces.write("    network 192.168.1.0")
interfaces.write("    broadcast 192.168.1.255")
interfaces.close()
os.system("sudo apt-get install dnsmasq")
os.system("sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig")
dnsmasq = open("/etc/dnsmasq.conf","a")
dnsmasq.write("interface=eth0")
dnsmasq.write("listen-address=192.168.1.1")
dnsmasq.write("dhcp-range=192.168.1.50,192.168.1.100,12h")
dnsmasq.write("server=8.8.8.8")
dnsmasq.write("bind-interfaces")
dnsmasq.write("domain-needed")
dnsmasq.write("bogus-priv")
dnsmasq.close()
interface = open("/etc/network/interfaces", "a")
interface.write("auto wlan0")
interface.write("allow-hotplug wlan0")
interface.write("iface wlan0 inet manual")
interface.write("wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf")
interface.close()
print("Restart Your PI.")