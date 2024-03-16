import socket
import re
import time

class Netcat:
    def __init__(self, ip, port):

        self.buff = b""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 1024):
        return self.socket.recv(length)
 
    def read_until(self, data):
        while not data in self.buff:
            self.buff += self.socket.recv(1024)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):
        self.socket.send(data)
    
    def close(self):
        self.socket.close()

def recursive_dfs(graph, source, path):
    if source not in path:
        path.append(source)

    for neighbour in graph[source]:
        if neighbour not in path:
            print(source, neighbour)
            recursive_dfs(graph, neighbour, path)

    return path
    

def createGraph(data):
    fromNode = 0,
    toNode = 0,
    graph = {}

    for line in data.split("\n"):
        arrayOfNumbers = re.findall(r'\d+', line)

        if line[0] == '[':
            fromNode = arrayOfNumbers[3]
            toNode = arrayOfNumbers[2]

        if line[0] == 'N':
            if len(arrayOfNumbers) == 1:
                graph[arrayOfNumbers[0]] = []

            graph[arrayOfNumbers[0]] = arrayOfNumbers[1::]

    return [fromNode, toNode, graph]

nc = Netcat('ctf10k.root-me.org', 8001)

def sendReponse(data):
    graphData = createGraph(data)

    fromNode = graphData[0]
    toNode = graphData[1]
    graph = graphData[2]

    path = recursive_dfs(graph, fromNode, [])
    
    response = (toNode in path) and "yes" or "no"
    if len(path) == 0:
        response = "no"
    response += "\n"

    print("===========================================")
    print( graph, fromNode, toNode, response, path)

    nc.write( response.encode() )

    time.sleep(0)

while True:
    data = nc.read(4096).decode()
    if data:
        print(data)
        if data[0] == 'H':
            if data[1] == 'e':
                sendReponse(data)
        if data[0] == "O":
            sendReponse(data)
