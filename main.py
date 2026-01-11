from database import is_vehicle_allowed
from logger import log_vehicle
from datetime import datetime

def main():
    print("\n--- Smart Parking Access System ---")

    plate_number = input("Enter vehicle number: ").strip().upper()

    if is_vehicle_allowed(plate_number):
        print("\n✅ ENTRY GRANTED")
        print(f"Vehicle Number: {plate_number}")
        print(f"Time: {datetime.now()}")

        log_vehicle(plate_number, "ENTRY GRANTED")
    else:
        print("\n❌ ENTRY DENIED")
        print(f"Vehicle Number: {plate_number}")

        log_vehicle(plate_number, "ENTRY DENIED")

if __name__ == "__main__":
    main()
