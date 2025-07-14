# CAN UDS Fuzzing and Spoofing Simulator 🚗💣

This project simulates malicious activity and diagnostic testing on a virtual CAN Bus, focusing on UDS protocol.  
It includes fuzzing attack vectors, spoofed messages, and protocol behavior analysis.


## ⚙️ Setup Instructions

### 1. Enable virtual CAN interface (Linux only):
```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0

pip install python-can

python3 fuzzer.py

---

## 🎯 Goals

- Perform UDS-based fuzzing against a virtual ECU
- Inject spoofed CAN IDs with valid/invalid payloads
- Monitor, log, and analyze responses
- Demonstrate reverse engineering and security testing skills

---

## 🔧 Features

- [x] ISO-TP framed UDS message generation
- [x] Brute force on Service ID and Sub-functions
- [x] Spoof messages from different CAN IDs
- [x] Response logging and timestamping
- [x] Easy configuration of payloads

---

## 🧪 UDS Fuzzing Sample

```python
for sid in range(0x00, 0xFF):
    payload = [sid] + [random.randint(0x00, 0xFF) for _ in range(7)]
    send_can_message(spoof_id, payload)

---
