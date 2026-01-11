from datetime import datetime

LOG_FILE = "vehicle_log.txt"

def log_vehicle(plate_number, status):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{time_now} | {plate_number} | {status}\n"

    with open(LOG_FILE, "a") as file:
        file.write(log_entry)
