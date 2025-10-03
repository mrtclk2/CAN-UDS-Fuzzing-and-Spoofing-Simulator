###  CAN UDS Fuzzing & Spoofing Simulator

A Python-based toolset for simulating CAN Bus and UDS protocol security testing.  
Includes fuzzing, spoofing, sniffing, logging, and response analysis in a virtual CAN environment.  
Ideal for red team simulation, educational labs, and automotive cybersecurity learning.

---

## Features

-  Virtual CAN Bus simulation (`vcan0`)
-  UDS Service ID fuzzing
-  CAN message spoofing
-  Real-time sniffing & CSV logging
-  Response code interpretation (NRC parser)
-  Scenario-based testing structure

---

##  Components

| File / Folder | Description |
|---------------|-------------|
| `fuzzer.py` | Randomly sends spoofed UDS messages |
| `sniffer.py` | Listens and displays incoming CAN frames |
| `logger.py` | Logs messages to `logs/can_log.csv` |
| `response_parser.py` | Parses UDS responses (positive & negative) |
| `scenarios/` | Contains ready-to-run fuzzing scripts |
| `Usage.md` | Full usage instructions and workflow |
| `Example_scenarios.md` | Detailed explanation of implemented attack scenarios |

---

## Quick Setup

```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
pip install python-can
```

### Quick Start
```bash
# Terminal 1: Monitor traffic
python3 sniffer.py

# Terminal 2: Start fuzzing
python3 fuzzer.py

# (Optional) Terminal 3: Save log
python3 logger.py
```

### 📘 Documentation
- [📖 Usage Guide](./Usage.md)
- [🧪 Example Scenarios](./Example_scenarios.md)

