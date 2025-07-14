import can

# CONFIGURATION
interface = 'virtual'  # use 'socketcan' for physical CAN interface
channel = 'vcan0'      # or 'can0' for real CAN

def main():
    print("[*] Listening on CAN interface:", channel)
    bus = can.interface.Bus(channel=channel, bustype=interface)

    try:
        while True:
            msg = bus.recv()  # blocking call
            if msg is not None:
                print(f"[RX] ID=0x{msg.arbitration_id:X} DLC={msg.dlc} Data={msg.data.hex(' ').upper()}")
    except KeyboardInterrupt:
        print("\n[!] Sniffer stopped by user.")

if __name__ == "__main__":
    main()
