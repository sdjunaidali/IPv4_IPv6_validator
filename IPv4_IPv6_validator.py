#!/usr/bin/env python
def  check_IP( s):
    is_ipv4 = True
    is_ipv6 = True
    
    #check if IPv4
    numbers = s.split(".")
    if len(numbers) != 4:
        is_ipv4 = False
    if (is_ipv4):
        for x in numbers:
            if not x.isdigit():
                is_ipv4 = False
            i = int(x)
            if i < 0 or i > 255:
                is_ipv4 = False
            
    #check if IPv6
    if not is_ipv4:
        numbers = s.split(":")
        if len(numbers) != 8:
            is_ipv6 = False
        for x in numbers:
            #check if exadecimal 
            try:
                is_hex = int(x, 16)
            except:
                is_ipv6 = False
                break;
        #if here, every number was hexadecimal
        
    if is_ipv4:
        print "IPv4"
    elif is_ipv6:
        print "IPv6"
    else:
        print "Neither"
        

N = int(raw_input("Insert N: "))
for i in range(0,N):
    addr = raw_input("Insert address: ")
    check_IP(addr)