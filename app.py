from flask import Flask, render_template
import os

app = Flask(__name__)

LOG_FILE = "vehicle_log.txt"

def read_logs():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 3:
                    logs.append({
                        "time": parts[0],
                        "plate": parts[1],
                        "status": parts[2]
                    })
    return logs[::-1]  # show latest first

@app.route("/")
def dashboard():
    logs = read_logs()
    return render_template("dashboard.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
