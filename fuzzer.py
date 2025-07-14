import can
import random
import time

# CONFIGURATION
interface = 'virtual'  # 'socketcan' for real CAN, 'virtual' for testing
channel = 'vcan0'      # Use vcan0 for virtual, can0 for real
spoof_id = 0x7E0       # Typical Tester -> ECU ID
interval = 0.1         # Time between messages (seconds)

def generate_payload():
    # Random UDS service ID and parameters
    sid = random.randint(0x00, 0xFF)
    payload = [sid] + [random.randint(0x00, 0xFF) for _ in range(7)]
    return payload

def send_fuzz_message(bus, can_id, payload):
    msg = can.Message(arbitration_id=can_id,
                      data=payload,
                      is_extended_id=False)
    try:
        bus.send(msg)
        print(f"[+] Sent: ID=0x{can_id:X} Data={payload}")
    except can.CanError:
        print("[!] Message NOT sent")

def main():
    print("[*] Starting UDS Fuzzing on CAN Bus")
    bus = can.interface.Bus(channel=channel, bustype=interface)

    try:
        while True:
            data = generate_payload()
            send_fuzz_message(bus, spoof_id, data)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n[!] Stopped by user")

if __name__ == "__main__":
    main()
