import pyshark

def perform_traffic_analysis():
    print("\033[92mStarting Traffic Correlation Analysis...\033[0m")
    try:
        capture = pyshark.LiveCapture(interface='eth0')
        print("\033[92mCapturing 10 packets:\033[0m")
        capture.sniff(packet_count=10)
        for packet in capture.sniff_continuously(packet_count=10):
            print(f'Packet: {packet}')
    except Exception as e:
        raise RuntimeError(f"Failed to perform traffic analysis: {e}")
