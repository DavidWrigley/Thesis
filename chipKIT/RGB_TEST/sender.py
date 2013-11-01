import socket
import time
import threading

TCP_IP = "192.168.1.190"
TCP_PORT = 8888
BUFFER_SIZE = 1024

while(True):
        try:
                sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_STREAM) # TCP
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.settimeout(5)
                sock.bind(('',0))
                sock.connect((TCP_IP, TCP_PORT))
                print "connected"
                break
        except socket.timeout:
                print "timeout"
                time.sleep(4)

def Send():
        sock.send("r")
        time.sleep(1)
        sock.send("g")
        time.sleep(1)
        sock.send("b")
        time.sleep(1)
        toggle = 8
        message = ""
        while True:
                 
                layer = raw_input("layer: ")
                pixel = raw_input("pixel: ")
                red = raw_input("red: ")
                green = raw_input("green: ")
                blue = raw_input("blue: ")
                message += ( str(unichr(int(layer))) + str(unichr(int(pixel))) + str(unichr(int(red))) + str(unichr(int(green))) + str(unichr(int(blue))) )
                sock.send(message)
                message = ""
                
                """
                for i in range(8):
                        message += ( str(unichr(int(i))) + str(unichr(int(63))) + str(unichr(int(toggle))) + str(unichr(int(0))) + str(unichr(int(0))) )
                if(toggle == 8):
                        toggle = 0
                else:
                        toggle = 8
                sock.send(message)
                time.sleep(2)
                message = ""
                """
        
def Receive():

        while True:
                try:
                        data, addr = sock.recvfrom(BUFFER_SIZE) # buffer size is 1024 bytes
                        print "Received: ", data
                except socket.timeout:
                        a = 1

t1 = threading.Thread(target = Send)
t2 = threading.Thread(target = Receive)
print "threads started";
t1.start()
t2.start()
