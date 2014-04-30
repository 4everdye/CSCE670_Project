__author__ = 'Seward'
import socket
import re

class MyNER(object):
    pattern = re.compile(r'<([A-Z]+?)>(.+?)</\1>')

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def ner(self, text):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        for s in ('\f', '\n', '\r', '\t', '\v'):
            text = text.replace(s, '. ')
        text += "\n"
        sock.send(text.encode('utf-8'))
        data = sock.recv(len(text) * 16)
        sock.close()
        matches = self.pattern.findall(data)
        ret = {}
        for type, content in matches:
            if type not in ret:
                ret[type] = []
            ret[type].append(content)
        return ret
