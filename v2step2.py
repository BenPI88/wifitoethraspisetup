import os
os.system("sudo apt-get update")
sysctl = open("/etc/sysctl.conf", "a")
sysctl.write("\nnet.ipv4.ip_forward=1")
sysctl.close()
os.system('sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"')
os.system('sudo bash && ipt="/sbin/iptables" && $ipt -P INPUT ACCEPT && $ipt -P FORWARD ACCEPT && $ipt -P OUTPUT ACCEPT && $ipt -F && $ipt -X && $ipt -t nat -F && $ipt -t nat -X && $ipt -t mangle -F && $ipt -t mangle -X && $ipt -t raw -F && $ipt -t raw -X')
os.system("sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE")
os.system("sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT")
os.system("sudo iptables -A FORWARD =i eth0 -o wlan0 -j ACCEPT")
os.system('sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"')
def removelastline(file):
  with open(file, 'r+') as fp:
    # read an store all lines into list
    lines = fp.readlines()
    # move file pointer to the beginning of a file
    fp.seek(0)
    # truncate the file
    fp.truncate()

    # start writing lines except the first line
    # lines[1:] from line 2 to last line
    fp.writelines(lines[1:])
    fp.close()
removelastline("/etc/rc.local")
rc = open("/etc/rc.local", "a")
rc.write("\niptables-restore < /etc/iptables.ipv4.nat\nexit 0")
rc.close
