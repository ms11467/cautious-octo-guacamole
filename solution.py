from socket import *
import os
import sys
import struct
import time
import select
import binascii
import socket
import math

ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 1
# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise.
# We shall use the same packet that we built in the Ping exercise

def checksum(string):
# In this function we make the checksum of our packet
    csum = 0
    countTo = (len(string) // 2) * 2
    count = 0

    while count < countTo:
        thisVal = (string[count + 1]) * 256 + (string[count])
        csum += thisVal
        csum &= 0xffffffff
        count += 2

    if countTo < len(string):
        csum += (string[len(string) - 1])
        csum &= 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def build_packet():
    #Fill in start
    # In the sendOnePing() method of the ICMP Ping exercise ,firstly the header of our
    # packet to be sent was made, secondly the checksum was appended to the header and
    # then finally the complete packet was sent to the destination.

    # Make the header in a similar way to the ping exercise.
    bpChecksum = 0
    bpID = os.getpid() & 0xFFFF
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, bpChecksum, bpID, 1)
    data = struct.pack("d", time.time())

    # Append checksum to the header.
    bpChecksum = checksum(header + data)
    if sys.platform == 'darwin':
        bpChecksum = htons(bpChecksum) & 0xffff
    else:
        bpChecksum = htons(bpChecksum)
    # Don’t send the packet yet , just return the final packet in this function.
    #Fill in end

    # So the function ending should look like this
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, bpChecksum, bpID, 1)
    packet = header + data
    return packet

def get_route(hostname):
    timeLeft = TIMEOUT
    tracelist1 = [] #This is your list to use when iterating through each trace 
    tracelist2 = [] #This is your list to contain all traces
    destAddr = gethostbyname(hostname) 
    
    for ttl in range(1,MAX_HOPS):
        for tries in range(TRIES):

            #Fill in start
            icmp = socket.getprotobyname("icmp")
            # Make a raw socket named mySocket
            #mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
            mySocket = socket.socket(AF_INET, SOCK_RAW, icmp)

            #Fill in end
            
            mySocket.setsockopt(IPPROTO_IP, socket.IP_TTL, struct.pack('I', ttl))
            mySocket.settimeout(TIMEOUT)
            #print('myTraceRoute to (' + hostname + '), ' + str(MAX_HOPS) + ' hops max.' + ' time out ' + str(TIMEOUT))
            try:
                d = build_packet()
                mySocket.sendto(d, (hostname, 0))
                t= time.time()
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                howLongInSelect = (time.time() - startedSelect)
                if whatReady[0] == []: # Timeout
                    #tracelist1.append("* * * Request timed out.")
                    #Fill in start
                    print ("*    *    * Request timed out.")
                    #You should add the list above to your all traces list
                    tracelist2.append(tracelist1)
                    #Fill in end
                recvPacket, addr = mySocket.recvfrom(1024)
                #print(addr)
                timeReceived = time.time()
                timeLeft = timeLeft - howLongInSelect
                if timeLeft <= 0:
                    tracelist1.append("* * * Request timed out.")
                    #Fill in start
                    #print ("*    *    * Request timed out.")
                    #You should add the list above to your all traces list
                    tracelist2.append(tracelist1)
                    #Fill in end
            except timeout:
                continue

            else:
                #Fill in start
                #Fetch the icmp type from the IP packet
                icmpHeader = recvPacket[20:28]
                types, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)
                #print("[types: ", types, "hostname: ]", dest)
                #Fill in end
                tracelist1 = []
                try:#try to fetch the hostname
                    #Fill in start
                    dest = gethostbyname(hostname)
                    #print("types: ", types, ": hostname: ", dest)
                    #print ("hostname: ", dest)
                    #tracelist1.append(gethostbyaddr(str(addr[0]))[0])
                    myVar1 = gethostbyaddr(str(addr[0]))[0]
                    #Fill in end
                except herror:   #if the host does not provide a hostname
                    #Fill in start
                    print("hostname not returnable")
                    #tracelist1.append("host not returnable")
                    myVar1 = "host not returnable"
                    #continue
                    #Fill in end

                if types == 11:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    #Fill in start
                    print("['{0}', '{1}ms', '{2}', '{3}'] ".format(ttl, ((timeReceived -t) * 1000), addr[0], hostname))
                    #You should add your responses to your lists here
                    tracelist1.append(ttl)
                    tracelist1.append("%.0fms" %((timeReceived - t) * 1000))
                    tracelist1.append(addr[0])
                    tracelist1.append(myVar1)
                    tracelist2.append(tracelist1)
                    #Fill in end
                elif types == 3:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    #Fill in start
                    print("['{0}', '{1}ms', '{2}', '{3}'] ".format(ttl, ((timeReceived -t) * 1000), addr[0], hostname))
                    #You should add your responses to your lists here 
                    tracelist1.append(ttl)
                    tracelist1.append(addr[0])
                    tracelist1.append(myVar1)
                    tracelist2.append(tracelist1)
                    #print (" %d rtt=%.0f ms %s" % (ttl,(timeReceived -t) * 1000, addr[0]))
                    #Fill in end
                elif types == 0:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    #Fill in start
                    print("['{0}', '{1}ms', '{2}', '{3}'] ".format(ttl, ((timeReceived -t) * 1000), addr[0], hostname))
                    #You should add your responses to your lists here and return your list if your destination IP is met
                    tracelist1.append(ttl)
                    tracelist1.append("%.0fms" %((timeReceived - timeSent) * 1000))
                    tracelist1.append(addr[0])
                    tracelist1.append(myVar1)
                    tracelist2.append(tracelist1)
                    #if str(addr[0]) == str(destAddr): 
                        #print ("addr[0]: ", addr[0], "destAddress: ", destAddr)
                    print ("tracelist2: \n", tracelist2)
                    print ("Host IP Test Passed!")
                        #print ("tracelist1: \n", tracelist1)
                    #print (" %d rtt=%.0f ms %s" % (ttl,(timeReceived -t) * 1000, addr[0]))
                    #Fill in end
                    return(tracelist2)
                else:
                    #Fill in start
                    #If there is an exception/error to your if statements, you should append that to your list here
                    tracelist1.append("error")
                    tracelist2.append("error")
                    #print ("hostname not returnable")
                    #Fill in end
                break
            finally:
                mySocket.close()
'''
print('++++++++++++++++++++++++++++++++++++++++++')
print('google.com')
print('++++++++++++++++++++++++++++++++++++++++++')
get_route("www.google.com") # USA - NA
print('++++++++++++++++++++++++++++++++++++++++++')
print('war.ukraine.ua')     
print('++++++++++++++++++++++++++++++++++++++++++')
get_route("war.ukraine.ua") # Ukraine   -   Warzone
print('++++++++++++++++++++++++++++++++++++++++++')
print('www.amamzon.in')          
print('++++++++++++++++++++++++++++++++++++++++++')
get_route("www.amazon.in") # India   -   Asia
print('++++++++++++++++++++++++++++++++++++++++++')
print('amamzon.co.uk')          
print('++++++++++++++++++++++++++++++++++++++++++')
get_route("amazon.co.uk") # UK      -   Europe
print('++++++++++++++++++++++++++++++++++++++++++')
print('sacoronavirus.co.za')          
print('++++++++++++++++++++++++++++++++++++++++++')
get_route("sacoronavirus.co.za") # Africa  -   South Africa
'''

if __name__ == '__main__':
    get_route("google.co.il")
#    get_route("bing.com")