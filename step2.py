import os
os.system("sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE")
os.system("sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT")
os.system("sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT")
print("If there is an error above, restart the pi. Otherwise move on to step 3!")
