import socket
import threading
from time import sleep

ip = "192.168.0.106"
port = 8000

class SocketClient:
    #定义一个ip协议版本AF_INET，为IPv4；同时也定义一个传输协议（TCP）SOCK_STREAM
    _client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    _connected = False
    
    def connect(self, server_ip_port=(ip,port)):
        #进行连接服务器
        try:
            self._client.connect(server_ip_port)
            self._connected = True
            self.send("i am client")
            
            while True:
                received_data=self._client.recv(1024)#接受服务端的信息，最大数据为1k
                print("->client receive data: %s" % received_data.decode('utf-8'))
                message=input("client wanna say:")
                self.send(message.encode('utf-8'))
        except Exception as ex:
            print("->connect to server error: %s" % ex)

    def send(self, message):
        try:
            if self._client:
                message = str(message).encode("utf-8")
                self._client.send(message)#将发送的数据进行编码
                print("->client send data: %s" % message)
        except Exception as ex:
            print("->send message error: %s" % ex)
            
    def close(self):
        try:
            if self._client:
                self._client.close()
                self._connected = False
        except Exception as ex:
            print("->disconnect from server error: %s" % ex)

class SocketServer:
    _server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def run_server(self, ip_port=(ip,port)):
        try:
            self._server.bind(ip_port)
            self._server.listen(3)
            client, _=self._server.accept()
            print(client)
        
            while True:
                received_data=client.recv(1024)#客户端发送的数据存储在recv里，1024指最大接受数据的量
                print("->server receive data: %s" % received_data.decode('utf-8'))
                message=input("server wanna say:")
                client.send(message.encode('utf-8'))
        except Exception as ex:
            print("->run server error: %s" % ex)
            
    def stop_server(self):
        try:
            if self._server:
                self._server.close()
        except Exception as ex:
            print("->stop server error: %s" % ex)


def run_server():
    server = SocketServer()
    # server.run_server(ip_port=("192.168.0.6", 8000))
    server.run_server()
    
def run_client():
    client = SocketClient();
    # client.connect(server_ip_port=("192.168.0.6", 8000))
    client.connect()

if __name__ == "__main__":
    t1 = threading.Thread(target=run_server)     # target是要执行的函数名（不是函数），args是函数对应的参数，以元组的形式存在
    t2 = threading.Thread(target=run_client)
    t1.start()
    sleep(1)
    t2.start()


