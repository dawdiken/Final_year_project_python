import socket
import fcntl
import struct
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ipadress = get_ip_address('wlan0')

with open('/home/pi/ipaddressfile.text', 'r') as myfile:
        textIp=myfile.read()


if ipadress != textIp:
    with open("/home/pi/ipaddressfile.text", "w") as text_file:
            text_file.write("%s" % ipadress)	
		fromaddr = "raspdhr@gmail.com"
		toaddr = "dawdiken@gmail.com"
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = get_ip_address('wlan0')

		body = "Python test mail"
		msg.attach(MIMEText(body, 'plain'))

		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login("raspdhr@gmail.com", "sidRonan")
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)


