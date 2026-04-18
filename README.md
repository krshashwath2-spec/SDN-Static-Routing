# SDN Static Routing using POX and Mininet

##  Project Overview
This project demonstrates **Static Routing using Software Defined Networking (SDN)**.  
The controller (POX) manually installs flow rules to control how packets travel in the network.

---

##  Objective
- Implement static routing using SDN
- Show packet forwarding and blocking
- Observe network behavior using Wireshark
- Understand controller–switch interaction

---

##  Network Topology

Hosts:
- h1 (Source)
- h2 (Destination - Allowed)
- h3 (Blocked)

Switches:
- s1, s2, s3, s4

Paths:
- Path 1: h1 → s1 → s2 → s3 → h2
- Path 2: h1 → s1 → s4 → s3 → h2

The controller selects **Path 1** for routing.

---

##  Technologies Used
- Mininet (Network Simulation)
- POX Controller (SDN Controller)
- OpenFlow Protocol
- Wireshark (Packet Analysis)

---

##  Setup & Execution

### 1. Start Controller
```bash
cd ~/pox
./pox.py log.level --DEBUG misc.demo_controller
