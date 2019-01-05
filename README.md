# CESRPB
Cisco Enable Secret Router Password Bruteforcer

Wrote this script after finding cisco devices listening on telnet on the public internet during routing pentesting engagements against clients.

Orginially tried writting this in pwntools but I had issues with the receiving end on telnet connections and decided to try using the pexpect library

EXAMPLE:
 	python cisco_router_bf.py -r 1.2.3.4 -f passwords.txt -n HOST -v no
