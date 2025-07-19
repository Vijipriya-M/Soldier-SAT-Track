import time
from datetime import datetime

log_file = "patrol_log.txt"

def send_direction_and_distance():
    direction = input("Enter direction (e.g., North, East, South, West): ").strip().upper()
    distance = input("Enter distance (e.g., 100m or 2km): ").strip()
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    
    log_entry = f"{direction} - {distance} at {timestamp}"
    with open(log_file, "a") as file:
        file.write(log_entry + "\n")
    print("☑️  Patrol data updated.\n")

def report_injury():
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    alert_entry = f"EMERGENCY: Possible Injury Reported at {timestamp}"
    with open(log_file, "a") as file:
        file.write(alert_entry + "\n")
    print("⚠️  Injury alert sent to base.\n")

def send_emergency_alert():
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    alert_entry = f"EMERGENCY: SOS Triggered at {timestamp}"
    with open(log_file, "a") as file:
        file.write(alert_entry + "\n")
    print("🚨 SOS alert sent to base.\n")

while True:
    print("===== 🪖 Soldier Action Panel =====")
    print("1. Send Direction & Distance")
    print("2. Report Injury")
    print("3. Send Emergency Alert")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ").strip()
    
    if choice == '1':
        send_direction_and_distance()
    elif choice == '2':
        report_injury()
    elif choice == '3':
        send_emergency_alert()
    elif choice == '4':
        print("📴 Soldier device exiting...")
        break
    else:
        print("❌ Invalid choice. Try again.\n")
