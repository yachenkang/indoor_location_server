from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH,ThreadingMixIn as TMI)    #可以通过as起别名
from time import ctime
from extract_fingerprint import extract
from insert import *

HOST = '192.168.1.105'
PORT = 1234
ADDR = (HOST, PORT)
class Server(TMI, TCP):                                         #变动位置  
    pass

class MyRequestHandler(SRH):
    def handle(self):
        print ('已经连接:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline().decode("UTF-8"))).encode("UTF-8"))
        request = str(self.request.recv(1024), encoding = "utf-8")
        print(request)
        self.request.sendall(bytes('OK',encoding = "utf-8"))
        #插入数据
        '''fingerprint=extract(request)
        print(fingerprint)
        storageOfFingerprint([1,5,8],fingerprint)
        data_view()'''

tcpServ = Server(ADDR, MyRequestHandler) 
print ('等待新的连接。。。。')

tcpServ.serve_forever()
