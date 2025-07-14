# CAN UDS Fuzzing and Spoofing Simulator 🚗💣

This project simulates malicious UDS diagnostic traffic over a virtual CAN Bus.  
It allows security testing of ECU behavior under fuzzed UDS Service IDs and spoofed CAN IDs using ISO-TP framed payloads.  
This tool is designed for cybersecurity learning, reverse engineering practice, and offensive security research in the automotive domain.

---

## 🎯 Goals

- Perform UDS-based fuzzing against a simulated ECU
- Inject spoofed CAN IDs with variable payloads
- Monitor, log, and analyze protocol behavior
- Demonstrate hands-on automotive red teaming

---

## 🔧 Features

- [x] ISO-TP compliant UDS message generation
- [x] Brute-force testing of Service IDs and subfunctions
- [x] Randomized spoofing from attacker CAN IDs
- [x] Logging with timestamp and message structure
- [x] Simple terminal interface, easy configuration

---

## 🧪 Sample Fuzzing Payload

```python
for sid in range(0x00, 0xFF):
    payload = [sid] + [random.randint(0x00, 0xFF) for _ in range(7)]
    send_can_message(spoof_id, payload)
