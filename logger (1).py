
import can
import csv
from datetime import datetime

# CONFIGURATION
interface = 'virtual'  # 'socketcan' for real CAN interface
channel = 'vcan0'
log_file = 'logs/can_log.csv'

def main():
    print("[*] Logging CAN messages on", channel)
    bus = can.interface.Bus(channel=channel, bustype=interface)

    with open(log_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CAN_ID", "DLC", "Data"])

        try:
            while True:
                msg = bus.recv()
                if msg:
                    timestamp = datetime.now().isoformat()
                    can_id = f"0x{msg.arbitration_id:X}"
                    dlc = msg.dlc
                    data = msg.data.hex(' ').upper()
                    print(f"[LOG] {timestamp} {can_id} DLC={dlc} Data={data}")
                    writer.writerow([timestamp, can_id, dlc, data])
        except KeyboardInterrupt:
            print("\n[!] Logging stopped by user.")

if __name__ == "__main__":
    main()
