from socket import *

HOST = '127.0.0.1'
PORT = 12323
BUFFSIZE = 10000
ADDRESS = (HOST, PORT)

RULE = {
    "A5 5A 55 00 FF FF 13 00 00 13 11 0D": "A5 5A 55 00 00 00 00 2D",
    "A5 5A 55 00 00 00 00": "A5 5A 55 00 00 00 00",
}

#tcpClientSocket = socket(AF_INET, SOCK_STREAM)
#tcpClientSocket.connect(ADDRESS)

s = socket()
s.bind(ADDRESS)

s.listen(10)

while True:
    conn,addr = s.accept()
    print(conn,addr)
    while True:
        try:
            data= conn.recv(1024)
            test = data.hex(' ')
            print(data.hex(' ').upper())
            if data.hex(' ').upper() in RULE.keys():
                conn.send(bytes.fromhex(RULE[data.hex(' ').upper()]))
                print(RULE[data.hex(' ').upper()])
        except:
            pass
    
print("链接已断开！")
tcpClientSocket.close()