import os
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
rc.write("iptables-restore < /etc/iptables.ipv4.nat")
rc.write("exit 0")
rc.close()
os.system("sudo service dnsmasq start")
print("Done! Please reboot the Raspberry Pi.")
