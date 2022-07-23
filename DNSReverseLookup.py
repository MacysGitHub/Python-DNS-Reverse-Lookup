import math
import socket
import random
import struct
import sys
import numpy

dnsServer = "255.255.255.255"

# num = numpy.uint16(random.randint(1000, 9999))
#
# print(sys.getsizeof(num))

#dnsQuery = struct.pack("iiiiiiii", num, 0, 0, 0, 0, 0, 0, 0)

def reversednslookup(ip):
    #DNS Header
    #test = struct.pack('>H', random.randint(1, 65535)) # DNS Query ID can be any 16-bit number
    test = struct.pack('>H', 1)
    #DNS Flags
    test += struct.pack('>H', 288)
    print(test)
    test += struct.pack('>H', 1) #Questions - we only have 1 question here
    test += struct.pack('>H', 0) #Answers - 0 is for query
    test += struct.pack('>H', 0) #Authorities
    test += struct.pack('>H', 0) # Should be set to 0
    test += struct.pack('>H', 1) # Additional RR's
    #print(test)
    #Now the question....
        #insert code here...
    splitip = ip.split(".")
    print(splitip)
    counter = 0
    for part in splitip:
        if(len(part) > 1):
            test += struct.pack('>B', len(part))
            partsplit = part.split()
            #print(partsplit)
            for sect in partsplit:
                last = list(sect)
                for l in last:
                    test += struct.pack("p", bytes(l, 'ascii'))
                    print("iter: " + str(counter) + " " + l)
                    counter += 1
            #test += struct.pack('>B', int(part))

    print(test)


true = reversednslookup(ip=dnsServer)


def dnsreverselookup():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect((dnsServer, 53))
    r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    r.bind((gethostbyname(gethostname), 53))
    while connect:
        result = s.send(dnsQuery)
        s.close()
        print(result)
        r.recv(1024)

    print(r)


#dnsreverselookup()
#print(dnsQuery.ID)