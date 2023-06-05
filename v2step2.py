import os
os.system("sudo apt-get update")
sysctl = open("/etc/sysctl.conf", "a")
sysctl.write("\nnet.ipv4.ip_forward=1")
