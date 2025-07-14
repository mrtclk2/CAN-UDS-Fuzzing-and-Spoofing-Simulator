# 🛰 How to Use sniffer.py

The `sniffer.py` script passively listens to a CAN interface and prints every incoming CAN message.  
It is designed for use with virtual interfaces like `vcan0`, and helps visualize fuzzed or spoofed traffic in real time.

---

### 🔧 Requirements

- Linux-based OS
- Python 3.x
- `python-can` library installed
- A configured CAN interface (virtual or physical)

---

### ⚙️ 1. Setup Virtual CAN Interface (`vcan0`)

```bash
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
```

### 📦 2. Install Dependencies

```bash
pip install python-can
```
### ▶️ 3. Run the Sniffer

Start the sniffer in one terminal:

```bash
python3 sniffer.py
```
You should see outputs like:
```bash
[RX] ID=0x7E0 DLC=8 Data=10 01 FF 3A 22 00 00 EF
[RX] ID=0x7E0 DLC=8 Data=2E F1 90 12 34 56 78 9A

```

### 🧪 4. Run the Fuzzer (Optional)
In a second terminal, start your fuzzer to generate traffic:

```bash
python3 fuzzer.py
```

