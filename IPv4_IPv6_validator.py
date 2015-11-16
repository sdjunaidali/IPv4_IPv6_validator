
import ipaddress


def  check_IP( s):
   try:
       
     ipaddress.ip_address(addr)
     is_ipv4 = True
     is_ipv6 = True
    
     #check if IPv4
     numbers = addr.split(".")
     if len(numbers) != 4:
        is_ipv4 = False
     if (is_ipv4):
        for x in numbers:
            if not x.isdigit():
                is_ipv4 = False
            i = int(x)
            if i < 0 or i > 255:
                is_ipv4 = False

     if is_ipv4:
        print ("The address {0} is IPv4".format(addr))      

     #If not IPv4 then It is IPv6 else throw error.
     if not is_ipv4:
         print("The address {0} is IPv6".format(addr))
         
        
   except ValueError as e:
            print(e)

if __name__ == '__main__':

    
    while True:
      addr = input("Insert address to validate: ")
    
      check_IP(addr)


    
