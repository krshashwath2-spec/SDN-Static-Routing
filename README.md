# SDN Static Routing using POX and Mininet

## Objective
To implement static routing in a Software Defined Network (SDN) using a POX controller by manually installing flow rules.

## Tools Used
- Mininet (Network Emulator)
- POX Controller
- OpenFlow Protocol
- Ubuntu Linux

## Topology
Hosts: h1, h2  
Switches: s1, s2, s3, s4  

Connections:
- h1 → s1
- s1 → s2 and s4
- s2 → s3
- s4 → s3
- s3 → h2

## Working
- Controller installs static flow rules.
- Packets follow predefined paths.
- No dynamic routing is used.

Path:
- h1 → s1 → s2 → s3 → h2
- h2 → s3 → s4 → s1 → h1

## Commands Used

Run POX Controller:
