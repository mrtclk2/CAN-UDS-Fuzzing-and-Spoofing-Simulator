# CAN-UDS Fuzzing & Spoofing – Setup Guide

### 🔧 Virtual CAN Setup (vcan0)

To simulate a CAN Bus environment without any physical ECU or vehicle, we will use a virtual CAN interface called `vcan0`. This allows safe and controlled fuzz testing.

```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

### 🛠 Install Python Dependencies

We use the python-can library to send CAN messages from Python.

```bash
pip install python-can
```
Make sure Python 3.x is installed and you're working inside a virtual environment if needed.

### ▶ Run the Fuzzer
Launch the fuzzing script:

```bash
python3 fuzzer.py
```
You’ll start to see outputs like:

```bash
[+] Sent: ID=0x7E0 Data=[0x10, 0x01, 0xFF, 0x3A, 0x22, 0x00, 0x00, 0xEF]
This indicates that spoofed and randomized UDS messages are being injected onto the virtual CAN bus.
```

### 📡 Monitor with Wireshark (Optional but Powerful)
If you want to inspect the traffic visually, Wireshark is a great tool.

Install and launch it:

```bash
sudo apt install wireshark
sudo wireshark &
```
Choose the interface vcan0 and apply this filter to view messages from spoofed tester (e.g., 0x7E0):

```bash
can.id == 0x7E0
```

### 📌 Summary of Commands

```bash
# Setup vcan0
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0


# Install dependencies
pip install python-can

# Run script
python3 fuzzer.py

# Optional: Wireshark
sudo apt install wireshark
sudo wireshark &
```
