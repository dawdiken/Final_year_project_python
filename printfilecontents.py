import fcntl
import struct
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print get_ip_address('wlan0')

file = open(/home/pi/ipaddressfile.text”, “r”) 
print file.read() 