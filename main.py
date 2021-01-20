from vidstream import StreamingServer
import threading


#use public or private or public ip in brackets
receiver = StreamingServer('192.168.0.17', 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()