# Usage Guide – CAN-UDS Fuzzing & Spoofing Simulator

This guide will walk you through the setup and usage of all core scripts in this project.  
It is designed for educational use in automotive cybersecurity and protocol fuzzing scenarios.

---

### 1. Environment Setup (vcan0)

To simulate a vehicle CAN bus without hardware, use Linux’s virtual CAN interface.

```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
You should now have a virtual CAN interface named vcan0.
```
### 2. Install Python Dependencies
Ensure Python 3.x is installed, then install required libraries:

```bash
pip install python-can
```

### 3. How to Use Each Script

# fuzzer.py
Randomly sends spoofed UDS messages over CAN.

```bash
python3 fuzzer.py
```
You’ll see outputs like:

```bash
[+] Sent: ID=0x7E0 Data=[0x10, 0x01, 0xFF, 0x3A, 0x22, 0x00, 0x00, 0xEF]
```

# 📡 sniffer.py
Listens to the CAN bus and prints all received messages.

```bash
python3 sniffer.py
```
Example output:

```bash
[RX] ID=0x7E0 DLC=8 Data=10 01 FF 3A 22 00 00 EF
```

# logger.py
Logs all CAN messages into a timestamped CSV file at logs/can_log.csv.

```bash
python3 logger.py
```
This creates a structured log of ID, DLC, and Data.

# response_parser.py
A helper module to interpret UDS responses.

```bash
from response_parser import parse_response

data = [0x7F, 0x10, 0x13]
result = parse_response(data)
print(result)  # NEGATIVE_RESPONSE to SID 0x10 → NRC 0x13
```

# scenarios/scenario1_bruteforce_sid.py
Brute-force all possible UDS Service IDs with randomized payloads.

```bash
python3 scenarios/scenario1_bruteforce_sid.py
```
Helps discover undocumented services or trigger ECU behaviors.

### 4. Suggested Workflow
Open Terminal 1:
```bash
python3 sniffer.py
```
Open Terminal 2:
```bash
python3 fuzzer.py
```
(Optional) Open Terminal 3:
```bash
python3 logger.py
```
