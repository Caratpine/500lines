import socket


def threaded_method():
    sock = socket.socket()
    sock.connect(('www.jianshu.com', 80))
    request = 'GET / HTTP/1.1\r\nHost: www.jianshu.com\r\nConnection: close\r\nUser-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    print(type(chunk))
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    print(response)


threaded_method()
