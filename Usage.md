
# 📘 Usage Guide

This repository simulates UDS fuzzing and spoofing on a CAN Bus using Python.

## Components

- `fuzzer.py` – Randomly sends spoofed UDS messages
- `sniffer.py` – Listens to CAN traffic in real-time
- `logger.py` – Logs CAN traffic to CSV
- `response_parser.py` – Analyzes UDS response messages
- `scenarios/scenario1_bruteforce_sid.py` – Brute-force SID testing

## Workflow

1. Set up your virtual CAN interface:
```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

2. Run `sniffer.py` or `logger.py` in one terminal to monitor traffic.
3. Run `fuzzer.py` or a scenario script in another terminal.
