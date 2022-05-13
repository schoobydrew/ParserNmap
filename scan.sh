#!/bin/bash
mkdir nmap
#nmap -sC -sV -oN nmap/standard $1
#nmap -sV --script safe -oN nmap/safe $1
#nmap --script vuln -oN nmap/vuln $1


#initial scan
nmap -p- -oN nmap/full $1
## get results
results=$(for i in $(cat nmap/full | grep open | awk -F/ '{ print $1 }'); do echo -n $i,; done)
nmap --script "default or safe" -sV -oN nmap/default-safe $1 -p $results
nmap -sC -sV -sU --top-ports 20 -oN nmap/udp20 $1
nmap -sU -sV -Pn --top-ports 1000 -oN nmap/udp1000 $1