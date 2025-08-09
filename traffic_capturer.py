import pyshark
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from config import CAPTURE_INTERFACE, PACKET_COUNT, RAW_DATA_FILE 

def capture_and_save_packets():
    print(f"Capturing {PACKET_COUNT} packets on interface {CAPTURE_INTERFACE}...")
    capture = pyshark.LiveCapture(interface=CAPTURE_INTERFACE, tshark_path="C:\\Users\\siddh\\OneDrive\\Desktop\\ai_traffic_analyzer\\Wireshark\\tshark.exe")
    packets = []

    for packet in capture.sniff_continuously(packet_count=PACKET_COUNT):
        try:
            packets.append({
                "Time": packet.sniff_time,
                "Source": packet.ip.src,
                "Destination": packet.ip.dst,
                "Protocol": packet.highest_layer,
                "Length": int(packet.length),
            })
        except AttributeError:
            continue

    os.makedirs(os.path.dirname(RAW_DATA_FILE), exist_ok=True)
    pd.DataFrame(packets).to_csv(RAW_DATA_FILE, index=False)
    print(f"Captured packets saved to {RAW_DATA_FILE}")

if __name__ == "__main__":
    capture_and_save_packets()
