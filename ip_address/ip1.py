# https://www.iditect.com/how-to/59143787.html 
# https://www.kite.com/python/docs/ipaddress.collapse_addresses


from ipaddress import IPv4Address,summarize_address_range,IPv4Network,collapse_addresses
#******************************************************************************************
#      print  all ip address in list of subnets 
#
try:
    nets =[IPv4Network("192.4.1.30/28",False),IPv4Network("10.10.4.0/30")]
    print ("\n ********** all ip address in list of subnets    ******* \n")

    for net in nets:
        for addr in net:
            print(addr)
except Exception as excp1:
    print("*** Error ***  Try again  ...  ",excp1)
#******************************************************************************************
#         Summerize   from  frist address fo last address
#
first = IPv4Address('10.182.71.0')
last = IPv4Address('10.182.75.255')
summary =summarize_address_range(first,last)
print ('\n\n**************   summery list  from 10.182.71.0   TO   10.182.75.255 is  **************\n')
for item in summary:
    print (item)
#*******************************************************************************************


#*******************************************************************************************
#      
#            collapse_addresses of list of networks    
iplist =[
    IPv4Network('10.105.200.15/30',False), 
    IPv4Network('10.105.1.0/27',False), 
    IPv4Network('10.105.205.0/27',False), 
    IPv4Network('10.105.205.32/27',False), 
    IPv4Network('10.105.205.64/26',False), 
    IPv4Network('10.105.205.128/25',False),
    IPv4Network('10.105.205.192/28',False),
    IPv4Network('10.105.205.208/29',False),
    ]
collapselist=collapse_addresses(iplist) 
print ('\n\n**************   collapse_addresses  from list      **************\n')

for item in collapselist:
    print (item)


print ('\n\n**************   End     **************\n')
