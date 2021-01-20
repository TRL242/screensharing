from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('192.168.0.17', 9999)

#use public or private or public ip in brackets
sender = ScreenShareClient('192.168.0.17', 9999)

t = threading.Thread(target=sender.start_server)
t.start()

while input("") != 'STOP':
    continue

sender.stop_server()